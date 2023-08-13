#! /usr/bin/env python3 
# above is interpretor line.


import rclpy
from rclpy.node import Node
# ti write node we import Node class

class MyNode(Node):

    def __init__(self):
        self.counter_ = 0
        super().__init__("py_test_class")
        # node name
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5 , self.timer_callback)

    # it is a callback function used to call in create_timer functiom
    def timer_callback(self):
        self.counter_ +=1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args =None):
    # implement ros2 communication main code
    # starts ros2 communication
    rclpy.init(args=args)

    # new node is created
    node = MyNode()

    # loging data   
    rclpy.spin(node)
    # It makes our code to be alive though it is not subscribing or publishing
    # timer will run and you see that line printed until you exit ( Node ends )

    # at the end shutdown
    rclpy.shutdown()

if __name__ == "__main__":
    main()