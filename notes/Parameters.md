* It is a configuration value for a node. Useful for anykind of setting
* Declare those parameters in your code.
* Value set at run time
* A parameter is specefic to a node
* Ros2 parameter types:
    * Boolean
    * Int
    * Double

* `ros2 param get /node param` => gives parameter in topic
    * nodes have to be running

* `ros2 run pkg_name node_name --ros-args -p param_name_1:=data_1 -p param_name_2:=data_2`
    * `-p` to change the parameter `param_name`