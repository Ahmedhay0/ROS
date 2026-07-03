from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def build_nodes(context):
    inp = LaunchConfiguration("robots").perform(context)

    robots = inp.split(";")

    nodes = []

    for r in robots:
        name, prio, x, y, theta = r.split(",")

        nodes.append(
            Node(
                package="fleet_emulation",
                executable="robot",
                name=name,
                output="screen",
                arguments=[name, prio, x, y, theta],
            )
        )

    return nodes


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument(
            "robots",
            description="Format: name,prio,x,y,theta;name2,prio2,x2,y2,theta2"
        ),

        OpaqueFunction(function=build_nodes),
    ])