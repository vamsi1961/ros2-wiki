# Launch File 

* Most of the time we run multiple nodes ( ex:- Taalker , publisher )
* Using multiple terminals is a tiring process. We add all nodes at once through launch file.We add all in a single script.

## Setup

* Create a new package with any name. conventional name :- robot_bringup. 
* Exclude `src/` and `include/` add new folder `launch/`

* Update `CMakeList.txt` according to launch folder

```cmake 
install(DIRECTORY
  launch
DESTINATION share/${PROJECT_NAME}
)
```

* create a python launch file `pythoncode.launch.py` and make it executable.
