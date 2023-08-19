#! /usr/bin/env python3 
# above is interpretor line.


import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

# this contains message types

class Pub(Node):

    def __init__(self):
        self.counter_ = 0
        super().__init__("publisher")

        self.declare_parameter("pub","value")
        self.data_ = self.get_parameter("pub").value


        self.publisher_ = self.create_publisher(String , "data" , 10)
        self.timer = self.create_timer(0.5 , self.publish)
        self.get_logger().info(" Publishing started")


        # arguments : msg_type , topic,, quesize
        # if some messages are lost in sending quesize elements are stored( buffer)
       

    def publish(self):
        msg = String()
        
        self.publisher_.publish(msg)



def main(args =None):

    rclpy.init(args=args)
    node = Pub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()