import rclpy
import random
from rclpy.node import Node
import math
from turtlesim.srv import Spawn
from functools import partial
from turtlesim.srv import Kill
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.srv import CatchTurtle


class TurtleSpawner(Node):

    def __init__(self):
        super().__init__("turtle_Spawner") 
        self.declare_parameter("spawn_frequency" , 1.0)
        self.declare_parameter("turtle_name_prefix" , "turtle")

        self.turtle_name_prefix_ = self.get_parameter("turtle_name_prefix").value
        self.spawn_frequency_ = self.get_parameter("spawn_frequency").value
        self.turtle_counter_ = 0
        self.alive_turtles_ = []
        self.alive_turtles_publisher_ = self.create_publisher(
            TurtleArray , "alive_turtles" , 10)
        self.spawn_turtle_timer_ = self.create_timer(1.0/self.spawn_frequency_ , self.spawn_new_turtle)
        # when turtle is reached to new turtle position it has to kill that and go to next turtle
        # we create a service

        self.catch_turtle_service_ = self.create_service(
            CatchTurtle , "catch_turtle" , self.callback_catch_turtle) 

    def callback_catch_turtle(self,request,response):
        self.call_kill_server(request.name)
        response.success = True
        return response

    def publish_alive_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.alive_turtles_
        self.alive_turtles_publisher_.publish(msg)

    def spawn_new_turtle(self):
        self.turtle_counter_ += 1
        name = self.turtle_name_prefix_ + str(self.turtle_counter_)
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0, 11.0)
        theta = random.uniform(0.0, 2*math.pi)
        self.call_spawn_server(name, x, y, theta)

    def call_spawn_server(self,turtle_name , x,y,theta):
        
        client = self.create_client(Spawn , "spawn")
        while not client.wait_for_service(1.0):
            # it waits for 1.0 sec. if time is not given it waits forever

            self.get_logger().warn("Waiting for server to spawn turtle ....")
        request = Spawn.Request()

        request.x = x
        request.y = y
        request.name = turtle_name
        request.theta = theta

        future = client.call_async(request)

        # wait for future
        future.add_done_callback(partial(self.callback_call_spawn , turtle_name=turtle_name , x=x,y=y,theta=theta))


    def callback_call_spawn(self ,future ,turtle_name , x,y,theta):

        try:
            response = future.result()
            if response.name != "":
            # if response is not empty
            
                self.get_logger().info("Turtle " + response.name + " is now alive")
                new_turtle = Turtle()
                new_turtle.name = response.name
                new_turtle.x = x
                new_turtle.y = y
                new_turtle.theta = theta
                self.alive_turtles_.append(new_turtle)
                self.publish_alive_turtles()

        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e,))


    def call_kill_server(self,turtle_name ):
        
        client = self.create_client(Kill , "kill")

    # wait for the server

        while not client.wait_for_service(1.0):
            # it waits for 1.0 sec. if time is not given it waits forever

            self.get_logger().warn("Waiting for server to spawn turtle ....")
        request = Kill.Request()
        request.name = turtle_name

        future = client.call_async(request)

        # wait for future
        future.add_done_callback(partial(self.callback_call_kill , turtle_name=turtle_name ))


    def callback_call_kill(self ,future ,turtle_name):

        try:
            future.result()
            # though there is no response we so exception for response.
            # Raise an exception if request is not raised

            for (i,turtle) in enumerate(self.alive_turtles_):
                if turtle.name == turtle_name:
                    del self.alive_turtles_[i]
                    self.publish_alive_turtles()
                    break
            

        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e,))




def main(args = None):

    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

    