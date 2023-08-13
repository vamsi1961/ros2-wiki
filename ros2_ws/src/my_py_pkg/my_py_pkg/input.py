import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from std_msgs.msg import Empty
from my_robot_interfaces.srv import Input


class AddTwoIntsServerNode(Node): 

    def __init__(self):
        super().__init__("add_two_ints_server") 
        self.server_ = self.create_service(Input,"add_two_ints",self.callback_add_two_ints)
        self.publisher_ = self.create_publisher(Empty , "input_at_waypoint/input" , 10)
        #self.timer = self.create_timer(0.5 , self.publish)
        self.get_logger().info("Add two ints server started.")


    def callback_add_two_ints(self,request,response):
        response.response_message = request.request_message
        self.get_logger().info(str(request.request_message) + "=" + str(response.response_message))
        msg = Empty()
        
        self.publisher_.publish(msg)
        return response


def main(args = None):

    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    