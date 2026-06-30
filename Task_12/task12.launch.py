from launch import LaunchDescription
from launch.actions import  ExecuteProcess

def generate_launch_description():
    run_fleet= ExecuteProcess(
        cmd=['python3', '/home/ahmed/Desktop/task12_ws/src/fleet_emulator.py'],
        output="screen"
    )
    check_state= ExecuteProcess(
        cmd=["gnome-terminal","--","ros2","topic","echo","/States"],
        output="screen"
    )
    check_pose= ExecuteProcess(
        cmd=["gnome-terminal","--","ros2","topic","echo","/Positions"],
        output="screen"
    )
    check_prio= ExecuteProcess(
        cmd=["gnome-terminal","--","ros2","topic","echo","/Priorities"],
        output="screen"
    )
    graph= ExecuteProcess(
        cmd=["gnome-terminal","--","rqt"],
        output="screen"
    )
    return LaunchDescription([
        run_fleet,
        check_state,
        check_pose,
        check_prio,
        graph
    ])