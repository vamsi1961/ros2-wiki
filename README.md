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


## Nodes

Nodes are used to communicate data 

It is a subprogram in your application, responsible for only one thing.

Combiined to a graph

Communicatewith each other through topics, servers and parameters.

Reduce code complexity

Fault tolerance

Can be written in python , C++


To make code executable

    chmod +x <code.py>

To run it

    ./code.py


setup.cfg tells where you have to install the file

setup.py 

## Install the node

In ros2 we install the file into your workspace, because if you always want to run your node 
from the terminal directly like that, it's not scalable and you will be have much more 
functionalities if you install the file and we will see the benifts a little bit later.

We have to make changes in setup.cfg as well.

We make an executable by making some changes in setup.py 

    entry...

        'py_node = my_py_pkg.my_first_node:main'

        It will copy it and make some modifications so it becomes an executable for us

        Executable will be installed in the install folder of Ros2 workspace

        After building it a package is created in install folder

        before executing node which is installed do source ~/.bashrc







