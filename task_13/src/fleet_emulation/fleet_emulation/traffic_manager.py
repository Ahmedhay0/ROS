from math import hypot
import os
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
 
state_file = "/tmp/robots_state.txt"
 
 
def load_state():
    positions = {}
    priorities = {}
 
    if not os.path.exists(state_file):
        return positions, priorities
 
    with open(state_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 5:
                continue
            name, x, y, theta, prio = parts
            try:
                positions[name] = {"x": float(x), "y": float(y), "theta": float(theta)}
                priorities[name] = int(prio)
            except ValueError:
                continue
 
    return positions, priorities
 
 
def save_state(positions, priorities):
    with open(state_file, "w") as f:
        for name in positions:
            if name not in priorities:
                continue
            x = positions[name]["x"]
            y = positions[name]["y"]
            theta = positions[name]["theta"]
            prio = priorities[name]
            f.write(f"{name},{x},{y},{theta},{prio}\n")
 
 
def manage(robot, msg):
 
    robots_positions, robots_priorities = load_state()
 
    if isinstance(msg, Pose2D):
        robots_positions[robot.name] = {
            "x": msg.x,
            "y": msg.y,
            "theta": msg.theta
        }
 
    elif isinstance(msg, Int32):
        robots_priorities[robot.name] = msg.data
 
    save_state(robots_positions, robots_priorities)
 
    x = robot.pose.x
    y = robot.pose.y
    prio = robot.prio.data
 
    for other_robot in robots_positions:
 
        if other_robot == robot.name:
            continue
 
        if other_robot not in robots_priorities:
            continue
 
        other_x = robots_positions[other_robot]["x"]
        other_y = robots_positions[other_robot]["y"]
        other_priority = robots_priorities[other_robot]
 
        distance = hypot(
            x - other_x,
            y - other_y
        )
 
        if distance <= 4 and other_priority > prio:
            robot.danger = True
 
    if not robot.danger:
        return f"[CLEAR] {robot.name} path is clear"
    else: return f"[DANGER] {robot.name}"

