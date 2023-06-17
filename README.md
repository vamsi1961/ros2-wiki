# Ros2_Doc


It can be reused.

We no need to re-invent wheel 

When we are working with many sensors actuators adn lots of stuff ros2 is easy to integrate.


It provide ways of seperating your code into reusable blocks, along with set of communication tools between all your programs. 

It provides huge amount of tools and plug and play and saves huge amount of time. 

After installing the humble

run the demo files which are given while installing

This is basic talker and listener

    ros2 run demo_nodes_cpp talker

    ros2 run demo_nodes_cpp listener

A build tool is required. => colcon build

## Create a python package

    ros2 pkg create <package_name> --build-type ament_python --dependencies rclpy

    I main folder a package folder is created in that codes are written

    test => test files are written. 

    use "pip3 install setuptools==58.2.0". if python is depreciating

## Create a cpp package

    ros2 pkg create <package_name> --build-type ament_cmake --dependencies rclcpp

    In this include and src directory is present




If you want to build only one package 

    colcon build --packages-select my_cpp_pkg


