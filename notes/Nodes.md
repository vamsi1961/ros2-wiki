# Nodes

* Each node in ROS2 should be responsible for a single, modular purpose.
* Each node can send and recieve data from other nodes via topics, services, actions and parameters.
* A single executable program can contain one or more nodes.

* Camera package may contain fllowing nodes

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

        touch my_first_node.py

* Basic python node

        #! /usr/bin/env python3 
        # above is interpretor line.


        import rclpy
        from rclpy.node import Node
        # ti write node we import Node class


        def main(args =None):
            # implement ros2 communication main code
            # starts ros2 communication
            rclpy.init(args=args)

            # new node is created
            node = Node("py_test")

            # loging data
            node.get_logger().info("Hello ROS2")

            
            rclpy.spin(node)
            # It makes our code to be alive though it is not subscribing or publishing


            # at the end shutdown
            rclpy.shutdown()

        if __name__ == "__main__":
            main()


* Setup in an executable

    * Inform ros2 to make exetuable and specify it in entry point to the program. Update `entry_point` in the `setup.py` file

            entry_points={
                'console_scripts': [
                    "py_node = my_py_pkg.my_first_node:main"
                                    ],
                        }

    * `py_node` is the name of the new node executable 
    * It will be installed in `ros2_ws/src/install/my_py_pkg/lib/my_py_pkg/py_node` location  

* Make it an executable
    * `chmod +x my_first_node.py`

### Run Program

* After creating node, making it executable.
* Do `colcon build` in `src` directory. 
    * Now node is ready to run

* Source the current ros2 environment by running following command from the `src` dirctory

        source ./install/setup.bash

    * It will source your current workspace

* Run the node 

        ros2 run my_py_pkg py_node

* `py_node` is the node name which we gave in `setup.py`. 

## Python Node with Oops


























## Tasks

### ros2 run

* `ros2 run <pkg_name> <executable_name>` => command `ros2 run` launches an executable from a package

* 