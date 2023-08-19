from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    ld = LaunchDescription()

    pub_names = ["node1","node2","node3","node4","node5"]

    pub_nodes = []

    for name in pub_names:
        pub_nodes.append(Node(
            package = "my_py_pkg",
            executable ="publisher",
            name = "publish" + name.lower(),
            parameters = [{
                "pub_name":name
            }]
        ))

    subscriber = Node(
        package= "my_py_pkg",
        executable = "subscriber",
        name = "subscriber"
    )

    for node in pub_nodes:
        ld.add_action(node)

    ld.add_action(subscriber)

    return ld


