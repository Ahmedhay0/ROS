import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import  ExecuteProcess


def generate_launch_description():
    pkg=get_package_share_directory('task14pkg')
    world_file =os.path.join(pkg, 'worlds', 'wall_maze.sdf')
    robot_file =os.path.join(pkg, 'urdf', 'omni_robot.urdf')
    gz=ExecuteProcess(
        cmd=['gz','sim',world_file],
        output="screen"
    )
    with open(robot_file, 'r') as infp:
        robot_description = infp.read()
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-string', robot_description,
            '-name', 'my_robot',
            '-x', '-5.7748', '-y', '-1.2401', '-z', '0.0600'
        ]
    )
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge_args',
        output='screen',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        ]
    )
    auto_node = Node(
        package='task14pkg',
        executable='auto_node',
        name='Mover',
        output='screen'
    )
    return LaunchDescription([
        gz,
        bridge_node,
        robot_state_publisher,
        spawn_entity,
        auto_node,


    ])