from Fleet import Fleet
from Drone import Drone
from Package import Package
from grid import Grid
from Weather_System import WeatherSystem
from Execution import run_all_missions
from simulation import simulation
import os

cur_os = os.name
def clear():
    if cur_os == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def main():
    fleet = Fleet()
    fleet.load_from_file()
    print("📂 Fleet state loaded.")
    
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    
    weather_system = WeatherSystem()

    while True:
        print("\n===== AEROPATH SYSTEM =====")
        print("1.  Add Drone")
        print("2.  Add Package")
        print("3.  Add No-Fly Zone")
        print("4.  Assign Packages")
        print("5.  Show Status")
        print("6.  Save System")
        print("7.  Load System")
        print("8.  Top Drones")
        print("9.  Start Flight Simulation  ✈️")
        print("10. Champions of Efficiency  🏆")
        print("11. Set Wind for Drone       🌬️")
        print("0.  Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            drone_id    = input("Drone ID: ").strip().upper()
            while True:
                try:
                    drone_mass  = float(input("Drone mass (kg): "))
                    if drone_mass > 0:
                        break
                    else: print("drone_mass can't be zero or negative")
                except ValueError:
                    print("❌ Invalid input, try again.")
            while True:
                try:
                    max_payload = float(input("Max payload (kg): "))
                    if max_payload > 0:
                        break
                    else: print("max_payload can't be zero or negative")
                except ValueError:
                    print("❌ Invalid input, try again.")
            while True:
                try:
                    battery     = float(input("Battery % [default 100]: ") or 100)
                    if battery > 0:
                        break
                    else: print("battery can't be zero or negative")
                except ValueError:
                    print("❌ Invalid input, try again.")
            
            drone = Drone(drone_id, drone_mass, max_payload, battery)
            fleet.add_drone(drone)
            clear()
            print(f"✅ Drone {drone_id} added.")

        elif choice == "2":
            package_id = input("Package ID: ").strip().upper()
            while True:
                try:
                    weight     = float(input("Weight (kg): "))
                    if weight > 0:
                        break
                    else: print("weight can't be zero or negative")
                except ValueError:
                    print("❌ Invalid input, try again.")
            
            while True:
                try:
                    x = float(input("Destination X: "))
                    y = float(input("Destination Y: "))
                    break
                except ValueError:
                    print("❌ Invalid input, try again.")
            package = Package(package_id, weight, (x, y))
            
            max_x, max_y = max(max_x, x), max(max_y, y)
            min_x, min_y = min(min_x, x), min(min_y, y)
            
            fleet.add_package(package)
            clear()
            print(f"✅ Package {package_id} → ({x},{y}) added.")

        elif choice == "3":
            while True:
                try:
                    x = float(input("Destination X: "))
                    y = float(input("Destination Y: "))
                    break
                except ValueError:
                    print("❌ Invalid input, try again.")
            fleet.add_no_fly_zone([(x, y)])
            

            max_x, max_y = max(max_x, x), max(max_y, y)
            min_x, min_y = min(min_x, x), min(min_y, y)
            clear()
            print("✅ No-fly zone added.")

        elif choice == "4":
            fleet.assign_packages()
            clear()
            print("✅ Packages assigned.")

        elif choice == "5":
            clear()
            fleet.show_status()

        elif choice == "6":
            fleet.save_to_file()
            clear()
            print("💾 Saved.")

        elif choice == "7":
            fleet.load_from_file()
            clear()
            print("📂 Loaded.")

        elif choice == "8":
            clear()
            print("\n🏆 Top Drones:")
            for d in fleet.top_drones():
                print(d)

        elif choice == "9": 
            if not fleet.drones:
                clear()
                print("❌ No drones in fleet.")
                continue
            if not fleet.packages:
                clear()
                print("❌ No packages to deliver.")
                continue
            fleet.save_to_file()
            grid = Grid(min_x - 5, max_x + 5, min_y - 5, max_y + 5)
            
            if fleet.no_fly_zones:
                grid.register_no_fly_zones([tuple(z) for z in fleet.no_fly_zones])

            all_paths, all_statuses = run_all_missions(grid, fleet, weather_system)

            clear()
            print("\n📊 MISSION SUMMARY")
            print(f"{'Drone':<12} {'Missions':<10} {'Status'}")
            print("─" * 40)
            for drone in fleet.drones:
                did     = drone.drone_id
                n       = len(all_paths.get(did, []))
                statuses = all_statuses.get(did, [])
                last_s  = statuses[-1] if statuses else "—"
                print(f"{did:<12} {n:<10} {last_s}")

            routes = []
            for drone in fleet.drones:
                segs = all_paths.get(drone.drone_id, [])
                flat = []
                for seg in segs:
                    flat.extend(seg)
                routes.append(flat if flat else [(0, 0)])

            wind_info = {d.drone_id: weather_system.get_wind(d.drone_id)
                         for d in fleet.drones}
            print("\n🎬 Launching visualization…")
            simulation(
                routes          = routes,
                drones          = fleet.drones,
                obstacles       = fleet.no_fly_zones,
                pre_planned     = True,
                all_paths_per_drone = all_paths,
                wind_info       = wind_info
            )

        elif choice == "10":
            from logger import get_champions
            champs = get_champions()
            clear()
            if not champs:
                print("⚠️  No logs yet.")
            else:
                print("\n🏆 CHAMPIONS OF EFFICIENCY")
                print(f"{'Rank':<6}{'Drone':<12}{'Missions':<10}{'Battery'}")
                print("─" * 42)
                for i, c in enumerate(champs, 1):
                    bar = "█" * int(c['battery_remaining'] / 10)
                    print(f"{i:<6}{c['drone_id']:<12}{c['missions_completed']:<10}"
                          f"{c['battery_remaining']:5.1f}%  {bar}")

        elif choice == "11":
            did   = input("Drone ID: ").strip().upper()
            while True:
                try:
                    power = float(input("Wind factor (1.0 = calm, 3.0 = strong): ") or 1)
                    # تم التصليح هنا: >= 1 عشان ميعملش Loop لا نهائي
                    if power >= 1:
                        break
                    else: print("power can't be less than 1")
                except ValueError:
                    print("❌ Invalid input, try again.")
                    
            weather_system.set_drone_wind(did, power)
            clear()
            print(f"🌬️  Wind for {did} set to {power:.1f}x")

        elif choice == "0":
            fleet.save_to_file()
            clear()
            print("💾 Saved. Goodbye 👋")
            break

        else:
            clear()
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()