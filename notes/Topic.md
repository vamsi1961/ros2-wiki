# Topic

* Topics are a vital element of the ROS graph that act as a bus for nodes to exchange messages.
* A node may publish data to any number of topics and simultaneously have subscriptions to any number of topics.

* As always, don’t forget to source ROS 2 in every new terminal you open.


## Command line

* `ros2 topic -h`

    * pub - Directly publish message to a topic from terminal
    * echo - prints data in topic 
    * list - Current Active topics
    * hz - frequency of topic
    * info - Info about particular topic name
    * bw - Bandwidth of topic
    * type - Type of message.

## Remapping

* Topics can be remapped in run without disturbing actual topic,node.
* `--ros-args --remap`

``` bash
* ros2 run <pkg_name> <exec_name> --ros-args -r __node:= <newnode_name> -r <topic_name> := <newtopic_name> 
```
