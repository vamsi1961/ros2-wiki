# Nodes

* Each node in ROS2 should be responsible for a single, modular purpose.
* Each node can send and recieve data from other nodes via topics, services, actions and parameters.
* A single executable program can contain one or more nodes.

Camera package may contain fllowing nodes

    * Camera driver node
    * image processing node
    * data recording node

* Reduces the code complexity
* Each node can be a different entity
* Supports different languages for different nodes.

### First Node

* required dependencies rclpy 
* create a node in python package `ros2_ws/src/my_py_pkg/my_py_pkg` create a file `my_first_node.py`

* Create file

    * 



## Tasks

### ros2 run

* `ros2 run <pkg_name> <executable_name>` => command `ros2 run` launches an executable from a package

* 