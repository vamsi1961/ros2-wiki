# Turtlesim

# Turtlesim-project

This is a simple turtle simulator . The `main -turtle` catches all turtles . 

## Sample Video
[turtlesim.webm](https://github.com/vamsi1961/Turtlesim/assets/51513859/dca15c58-51bc-4559-9556-4c5b3899cbf5)

## Pre-requisites
1. Ubuntu 22.04 LTS
2. ROS2-Humble 

#### Follow

1. Clone the repository.

```bash
git clone "https://github.com/vamsi1961/Turtlesim.git"
```

2. Navigate to source folder.

```bash
cd Turtlesim/src
```

3. Build the packages.

```bash
colcon build
```

4. Run the **launch** file.

```bash
ros2 launch ros2 launch turtlesim_launch turtlesim_catch_them_all.launch.py 
```

### Other Commands

* ros2 run turtlesim turtlesim_node

    * It opens turtle

* ros2 topic list


```bash

/parameter_events
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

```
