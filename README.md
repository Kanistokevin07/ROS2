# My Simple ROS 2 Robot

This is a simple ROS 2 Python package with:
- A 2-link robot URDF
- A talker node publishing "Hello ROS 2"
- A launch file to visualize the robot in RViz2

## Usage

```bash
# Build workspace
colcon build
source install/setup.bash

# Launch robot
ros2 launch my_simple_robot display.launch.py

# Run talker
ros2 run my_simple_robot talker
