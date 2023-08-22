# Package :

Packages are containers for the codes that we write. It is directory that contains the necessary files and resources for creating and mapping software components in ROS2.

* ament_cmake => C++
* ament_python => python

* `package.xml` is common for both types of packages to add dependencies

## C ++

    |--> include/
            |--> <package_name>/
    |--> src/
    |--> CMakeList.txt
    |--> package.xml

## Python Package

    |--> <package_name>/
    |--> resource/
    |--> test/
    |--> package.xml
    |--> setup.cfg
    |--> setup.py

## Building Package:

* `colcon build` => builds the package

* build a particular package
    colcon build --select-packages <pkg_name>

    # build python package
    colcon build --packages-select my_py_pkg

    # build C++ package
    colcon build --packages-select my_cpp_pkg

- [x] [CMakeLists.txt] : This defines the build instructions for the package using CMAke, specifying the source files, dependencies, and compilation settings

* For python packages we can update package without building using `--symlink-install`

    colcon build --packages-select my_py_pkg --symlink-install

Though codes can be updated they should have executables. Executables can be made using `chmod +x file`
