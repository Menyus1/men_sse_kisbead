from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_beadando',
            executable='sensor_node',
            name='sensor_node'
        ),
        Node(
            package='robot_beadando',
            executable='control_node',
            name='control_node'
        )
    ])
