import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation as funi
from matplotlib.ticker import MultipleLocator as loc
from matplotlib.path import Path
from matplotlib.lines import Line2D
import numpy as np


def make_plane_marker():
    verts_vertical = [
        ( 0.0,   0.8),
        ( 0.08,  0.3),
        ( 0.6,   0.0),
        ( 0.12, -0.15),
        ( 0.12, -0.45),
        ( 0.35, -0.6),
        ( 0.08, -0.65),
        ( 0.0,  -0.5),
        (-0.08, -0.65),
        (-0.35, -0.6),
        (-0.12, -0.45),
        (-0.12, -0.15),
        (-0.6,   0.0),
        (-0.08,  0.3),
        ( 0.0,   0.8),
    ]
    verts = [(y, -x) for x, y in verts_vertical]
    codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 2) + [Path.CLOSEPOLY]
    return Path(verts, codes)


PLANE_MARKER = make_plane_marker()

PALETTE = [
    "#e63946", "#2a9d8f", "#e9c46a", "#f4a261",
    "#457b9d", "#8338ec", "#06d6a0", "#fb5607",
    "#3a86ff", "#ff006e",
]


def _smooth_path(points, steps_per_unit=20):
    """Linearly interpolate a list of (x,y) waypoints into a dense array."""
    xs, ys = [], []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        dist = max(np.hypot(x1 - x0, y1 - y0), 0.01)
        n = max(int(dist * steps_per_unit / 10), 2)
        xs.extend(np.linspace(x0, x1, n, endpoint=False))
        ys.extend(np.linspace(y0, y1, n, endpoint=False))
    xs.append(points[-1][0])
    ys.append(points[-1][1])
    return np.array(xs), np.array(ys)


def simulation(routes, drones, obstacles=None, pre_planned=False,
               all_paths_per_drone=None, wind_info=None):

    if len(routes) != len(drones):
        print("Error: number of routes and drones don't match")
        return

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(15, 11))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")
    ax.grid(color="#1e2a38", linewidth=0.8, linestyle="--")
    ax.set_axisbelow(True)


    drone_data = []  

    for i, drone in enumerate(drones):
        color = PALETTE[i % len(PALETTE)]
        did = drone.drone_id

        if all_paths_per_drone and did in all_paths_per_drone:
            segments = all_paths_per_drone[did]
            all_pts = []
            for seg in segments:
                if seg:
                    if all_pts and all_pts[-1] == seg[0]:
                        all_pts.extend(seg[1:])
                    else:
                        all_pts.extend(seg)
            if not all_pts:
                all_pts = [(0, 0)]
        else:
            if pre_planned:
                all_pts = list(routes[i]) if routes[i] else [(0, 0)]
            else:
                r = routes[i]
                all_pts = [(0, 0)] + list(r) + list(reversed(r)) + [(0, 0)]

        if len(all_pts) > 1:
            px = [p[0] for p in all_pts]
            py = [p[1] for p in all_pts]
            ax.plot(px, py, color=color, alpha=0.25, linewidth=1.2,
                    linestyle="--", zorder=2)

        xs, ys = _smooth_path(all_pts)

        trail_line, = ax.plot([], [], color=color, linewidth=2.0,
                              alpha=0.7, zorder=3)

        scatter = ax.scatter([], [], s=380, marker=PLANE_MARKER,
                             color=color, edgecolors="white",
                             linewidths=0.6, zorder=6,
                             label=f"{did}" + (f"  wind:{wind_info[did]:.1f}x" if wind_info and did in wind_info else ""))

        n_missions = len(all_paths_per_drone[did]) if all_paths_per_drone and did in all_paths_per_drone else 1
        drone_data.append({
            "scatter": scatter,
            "trail": trail_line,
            "xs": xs,
            "ys": ys,
            "done": False,
            "color": color,
            "missions": n_missions,
            "drone_id": did,
        })

    all_x = np.concatenate([d["xs"] for d in drone_data])
    all_y = np.concatenate([d["ys"] for d in drone_data])
    pad = 10
    ax.set_xlim(all_x.min() - pad, all_x.max() + pad)
    ax.set_ylim(all_y.min() - pad, all_y.max() + pad)

    span_x = max(abs(all_x.max()), abs(all_x.min()))
    span_y = max(abs(all_y.max()), abs(all_y.min()))
    ax.xaxis.set_major_locator(loc(1 if span_x < 80 else 2 if span_x < 200 else 5 if span_x < 1000 else 10))
    ax.yaxis.set_major_locator(loc(1 if span_y < 80 else 2 if span_y < 200 else 5 if span_y < 1000 else 10))

    if obstacles:
        xo, yo = zip(*[tuple(o) for o in obstacles])
        ax.scatter(xo, yo, color="#ff4444", s=80, marker="s",
                   label="No-Fly Zone", zorder=4,
                   edgecolors="#cc0000", linewidths=1.5, alpha=0.85)

    # Base marker
    ax.scatter([0], [0], color="#00ff88", s=300, marker="*",
               label="Base (0,0)", zorder=7,
               edgecolors="#007744", linewidths=1.2)

    if wind_info:
        wind_lines = ["Wind Conditions:"]
        for did, w in wind_info.items():
            bar = "#" * int(min(w, 10)) + "-" * max(0, 10 - int(w))
            wind_lines.append(f"  {did}: [{bar}] {w:.1f}x")
        ax.text(0.01, 0.99, "\n".join(wind_lines),
                transform=ax.transAxes, fontsize=7.5,
                verticalalignment='top', color="#aaccff",
                fontfamily="monospace",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#0d1117",
                          edgecolor="#334455", alpha=0.85))

    max_frames = max(len(d["xs"]) for d in drone_data)

    status_text = ax.text(0.99, 0.01, "", transform=ax.transAxes,
                          fontsize=8, color="white", ha="right", va="bottom",
                          fontfamily="monospace",
                          bbox=dict(boxstyle="round,pad=0.4", facecolor="#0d1117",
                                    edgecolor="#334455", alpha=0.85))

    def animate(frame):
        artists = []
        status_lines = []

        for d in drone_data:
            if d["done"]:
                artists += [d["scatter"], d["trail"]]
                continue

            path_len = len(d["xs"])
            f = min(frame, path_len - 1)
            cx, cy = d["xs"][f], d["ys"][f]

            if frame >= path_len - 1 and abs(cx) < 0.5 and abs(cy) < 0.5:
                d["done"] = True
                d["scatter"].set_visible(False)
                d["trail"].set_data([], [])
            else:
                d["scatter"].set_offsets((cx, cy))
                trail_start = max(0, f - 60)
                d["trail"].set_data(d["xs"][trail_start:f+1],
                                    d["ys"][trail_start:f+1])

            pct = int(100 * f / max(len(d["xs"]) - 1, 1))
            status_lines.append(f"{d['drone_id']:10s} [x{d['missions']}] {pct:3d}%")
            artists += [d["scatter"], d["trail"]]

        if status_lines:
            status_text.set_text("\n".join(status_lines))
        artists.append(status_text)
        return artists

    ani = funi(fig, animate, frames=max_frames, blit=True, interval=5, repeat=False)

    ax.set_title("AeroPath -- Drone Fleet Simulation",
                 fontsize=14, fontweight="bold", color="white", pad=12)
    ax.set_xlabel("X Coordinate", fontsize=9, color="#8899aa")
    ax.set_ylabel("Y Coordinate", fontsize=9, color="#8899aa")
    ax.tick_params(colors="#556677")
    for spine in ax.spines.values():
        spine.set_edgecolor("#223344")

    legend = ax.legend(loc="upper right", framealpha=0.85,
                       facecolor="#0d1117", edgecolor="#334455",
                       labelcolor="white", fontsize=8)
    plt.tight_layout()
    plt.show()