from setuptools import setup

package_name = 'my_simple_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['my_simple_robot/launch/display.launch.py']),
        ('share/' + package_name + '/urdf', ['my_simple_robot/urdf/robot.urdf.xacro']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kanisto kevin',
    maintainer_email='kanistokevin007@gmail.com',
    description='Simple ROS 2 robot URDF + talker example',
    license='MIT',
    entry_points={
        'console_scripts': [
            'talker = my_simple_robot.nodes.talker:main',
        ],
    },
)
