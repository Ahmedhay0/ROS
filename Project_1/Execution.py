from logger import log_mission


def execute_flight(grid_obj, drone_id, plan, info, weather_system, drone_obj):
    """
    Execute a single delivery flight.
    Returns: (status_string, actual_path_coords_only)
    actual_path is a list of (x, y) tuples — ready for simulation.
    """
    safety = info['max_battery'] * 0.10
    actual_path = []
    reached_target = False

    wind = weather_system.get_wind(drone_id)
    if wind > 1.0:
        print(f"  ⚠️  Wind factor for {drone_id}: {wind:.1f}x  — increased battery drain!")

    for i, (node, t) in enumerate(plan):
        actual_path.append(node)   

        if not reached_target and node == info['target']:
            reached_target = True
            drone_obj.deliver_package()
            info.get('package_obj') and info['package_obj'].mark_delivered()

        if reached_target and node == (0, 0):
            drone_obj.return_to_base()
            log_mission(drone_id, drone_obj.missions_completed, drone_obj.battery)
            return "Mission Success", actual_path

        if drone_obj.should_return_home(node, safety_margin=safety):
            if node != (0, 0):
                print(f"  🔋 Low Battery at {node} — Emergency RTL!")
                grid_obj.cancel_reservation(plan, t)

                rtl_path, _ = grid_obj.find_path_time_aware(node, (0, 0), start_time=t)
                if rtl_path:
                    grid_obj.reserve_path(rtl_path)
                    for rtl_node, rtl_t in rtl_path[1:]:
                        wind = weather_system.get_wind(drone_id)
                        drain = drone_obj.mass * 9.81 * 0.005 * wind
                        drone_obj.drain_battery(drain)
                        actual_path.append(rtl_node)
                    drone_obj.return_to_base()
                    log_mission(drone_id, drone_obj.missions_completed, drone_obj.battery)
                    return "Emergency RTL", actual_path

                log_mission(drone_id, drone_obj.missions_completed, drone_obj.battery)
                return "Critical: Forced Landing", actual_path

        wind = weather_system.get_wind(drone_id)
        mass = (info['drone_mass'] + info['payload']) if not reached_target else info['drone_mass']
        drain = mass * 9.81 * 0.005 * wind
        drone_obj.drain_battery(drain)

    log_mission(drone_id, drone_obj.missions_completed, drone_obj.battery)
    return "Mission Ended", actual_path


def run_all_missions(grid_obj, fleet, weather_system):

    pkg_map = {p.package_id: p for p in fleet.packages}

    all_paths    = {d.drone_id: [] for d in fleet.drones}
    all_statuses = {d.drone_id: [] for d in fleet.drones}

    print("\n🚁 MULTI-MISSION FLEET STARTED\n")

    max_flights = len(fleet.packages) * len(fleet.drones) + 20
    flights_done = 0
    cycle = 0

    while flights_done < max_flights:
        cycle += 1

        grid_obj.reservation_table.clear()
        grid_obj.edge_reservation.clear()

        fleet.assign_packages()

        if all(p.status == "delivered" for p in fleet.packages):
            print("\n🏁 ALL PACKAGES DELIVERED!")
            break

        active_this_cycle = [
            d for d in fleet.drones
            if d.status == "delivering" and pkg_map.get(d.package_id) is not None
        ]
        if not active_this_cycle:
            remaining = [p for p in fleet.packages if p.status != "delivered"]
            if remaining:
                print(f"\n⚠️  {len(remaining)} package(s) could not be delivered "
                      f"(no valid path or insufficient battery).")
            break

        for drone in fleet.drones:
            if drone.status != "delivering":
                continue

            package = pkg_map.get(drone.package_id)
            if package is None or package.status == "delivered":
                drone.status = "idle"
                drone.package_id = None
                continue

            plan, _ = grid_obj.find_path_time_aware(
                drone.position, package.destination, start_time=0
            )
            if not plan:
                print(f"  ❌ {drone.drone_id}: No path to {package.destination} — skipping package.")
                drone.status = "idle"
                drone.package_id = None
                package.status = "waiting"
                continue

            # Build return leg
            back, _ = grid_obj.find_path_time_aware(
                package.destination, (0, 0), start_time=plan[-1][1]
            )
            full_plan = plan + (back[1:] if back else [])
            grid_obj.reserve_path(full_plan)

            info = {
                "battery":    drone.battery,
                "payload":    package.weight,
                "drone_mass": drone.mass,
                "target":     package.destination,
                "max_battery": 100,
                "package_obj": package,
            }

            wind = weather_system.get_wind(drone.drone_id)
            print(f"  ✈  {drone.drone_id} → {package.destination}  "
                  f"[wind={wind:.1f}x | battery={drone.battery:.1f}%]")

            status, path = execute_flight(
                grid_obj, drone.drone_id, full_plan, info, weather_system, drone
            )
            package.mark_delivered()
            print(f"     → {status}  (battery left: {drone.battery:.1f}%)")

            all_paths[drone.drone_id].append(path)
            all_statuses[drone.drone_id].append(status)
            flights_done += 1

        print(f"  — Cycle {cycle} done —\n")

    return all_paths, all_statuses