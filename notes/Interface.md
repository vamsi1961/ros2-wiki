# Interface

* Topic:
    * Name ( /number_count)
    * Msg Definition ( example_interfaces/msg/Int64)

* Service:
    * Name (/reset_number_count)
    * Srv definition (exampple_interfaces/srv/SetBool)

* Service contain Request and Response

* Msg definition => Colcon build  =>  Msg lang (C++,Python...) source code

**Note:** These are [example_interface](https://github.com/ros2/example_interfaces) and [common_interfaces](https://github.com/ros2/common_interfaces) 

* Msg can be included in Srv.
* Srv can't be included in Srv.

* To create a custom Msg or Srv. It is better to create a new package.

* Add dependencies in `package.xml`.
    *` <build_depend>rosidl_default_generators</build_depend>`
    * `<exec_depend>rosidl_default_runtime</exec_depend>`
    * `<member_of_group>rosidl_interface_packages</member_of_group>`


* Add find_package in `CMakeLists.txt`

    * `find_package(rosidl_default_generators REQUIRED)`

* After creating Msg/Srv make following changes in `CMakelists.txt`

        rosidl_generate_interfaces(${PROJECT_NAME}
            "msg/HardwareStatus.msg"
            "srv/ComputerRectangularArea.srv"
            "srv/Input.srv"
            )

* In `settings.json` add path to include Msg/Srv path in code.

* `ros2 interface list` => get list of interfaces
* `ros2 interface package_name` => interfaces int that package


