from math import hypot
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

robots_positions = {}
robots_priorities = {}


def manage(robot, msg):

    robot.name = robot.name

    if isinstance(msg, Pose2D):

        robots_positions[robot.name] = {
            "x": msg.x,
            "y": msg.y
        }

    elif isinstance(msg, Int32):

        robots_priorities[robot.name] = msg.data

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

        if distance <= 3 and other_priority > prio:
            robot.danger = True

    if not robot.danger:
        return f"[CLEAR] {robot.name} path is clear"
    else: return f"[DANGER] {robot.name}"