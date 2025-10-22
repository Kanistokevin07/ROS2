from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_share = os.path.join(
        os.getenv('AMENT_PREFIX_PATH').split(os.pathsep)[0], 'share', 'my_simple_robot')

    robot_description_file = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_file}]
        ),
    ])
