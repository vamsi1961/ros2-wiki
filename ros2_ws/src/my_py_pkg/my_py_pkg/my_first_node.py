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