#! /usr/bin/env python3 
# above is interpretor line.


import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from std_msgs.msg import Empty
# this contains message types

class Pub(Node):

    def __init__(self):
        self.counter_ = 0
        super().__init__("publisher")
        self.publisher_ = self.create_publisher(Empty , "data" , 10)
        self.timer = self.create_timer(0.5 , self.publish)
        self.get_logger().info(" Publishing started")


        # arguments : msg_type , topic,, quesize
        # if some messages are lost in sending quesize elements are stored( buffer)
       

    def publish(self):
        msg = Empty()
        
        self.publisher_.publish(msg)



def main(args =None):

    rclpy.init(args=args)
    node = Pub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()