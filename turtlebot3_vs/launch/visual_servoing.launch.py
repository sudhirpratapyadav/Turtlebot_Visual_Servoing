#!/usr/bin/env python3

from os.path import join
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Include the Gazebo launch file
    tb3_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(join(get_package_share_directory("turtlebot3_gazebo"), "launch", "empty_world.launch.py"))
    )

    urdf_file = join(get_package_share_directory('turtlebot3_vs'),
                              'urdf',
                              'box.urdf')
    

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'box',  # Name of the entity to spawn
            '-file', urdf_file,  # Path to the URDF file
            '-x', '1.2',  # Initial X position
            '-y', '0.2',  # Initial Y position
            '-z', '0.1'   # Initial Z position
        ],
        output='screen'
    )

    return LaunchDescription([
        tb3_sim,
        spawn_entity,
    ])