from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


def main(args = None):

    rclpy.init(args=args)
    node = Node("add_two_ints_client")
    client = node.create_client(AddTwoInts , "add_two_ints")

    # wait for the server

    while not client.wait_for_service(1.0):
        # it waits for 1.0 sec. if time is not given it waits forever

        node.get_logger().warn("Waiting for server Add For Two Ints ....")

    # create request object

    request = AddTwoInts.Request()

    request.a = 3
    request.b = 8

    future = client.call_async(request)
    # future object is an object that may be set in the future
    rclpy.spin_until_future_complete(node,future)

    try:
        response = future.result()
        node.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(response.sum))
    except Exception as e:
        node.get_logger().error("Service call failed %r" %(e,))


        
    rclpy.shutdown()


    

if __name__ == "__main__":
    main()

    