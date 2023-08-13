#! /usr/bin/env python3 
# above is interpretor line.


import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
# ti write node we import Node class

class Subscriber(Node):

    def __init__(self):
        super().__init__("subscriber")
        
        self.subscriber_ = self.create_subscription(String , "data",self.subscribe,10)
        self.get_logger().info("Subscriber started")
    # it is a callback function used to call in create_timer functiom
    def subscribe(self,msg):
        
        self.get_logger().info(msg.data)

def main(args =None):

    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()