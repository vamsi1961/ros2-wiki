import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClientNode(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("add_two_ints_client") # MODIFY NAME
        self.call_add_two_ints_server(6,7)


    def call_add_two_ints_server(self,a,b):
        # we will create a cliet, we create the request, 
        # we call the server and also then see how we can wait fot the response 
        

        # we are in the class so self.
        client = self.create_client(AddTwoInts , "add_two_ints")

    # wait for the server

        while not client.wait_for_service(1.0):
            # it waits for 1.0 sec. if time is not given it waits forever

            self.get_logger().warn("Waiting for server Add For Two Ints ....")
        request = AddTwoInts.Request()

        request.a = a
        request.b = b

        future = client.call_async(request)

        # wait for future
        future.add_done_callback(partial(self.callback_call_add_two_ints , a=a , b=b))


    def callback_call_add_two_ints(self ,future , a,b):

        try:
            response = future.result()
            self.get_logger().info(str(a) + "+" + str(b) + "=" + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e,))








def main(args = None):

    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    