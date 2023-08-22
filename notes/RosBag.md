# ROSBags

* It logs published data .
* Replaying the bag publishes nodes which it logged.

ros2 bag -h # for help

 # convert  Given an input bag, write out a new bag with different settings
 # info     Info about a bag to the screen
 # play     Play back ROS data from a bag
 # record   Record ROS data to a bag
 # reindex  Reconstruct metadata file for a bag
 # list     Info about available plugins to the screen



# run number_publisher node and then run below command

ros2 bag record /number -o number_data
 # -o is used to specify the output file name