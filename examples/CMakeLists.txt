cmake_minimum_required(VERSION 2.8.3)
project(examples)
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp rospy message_generation actionlib_msgs geometry_msgs std_msgs
)
################################################
## Declare ROS messages, services and actions ##
################################################
## Generate services in the 'srv' folder
add_service_files(
   FILES PoseAdd.srv
)
## Generate actions in the 'action' folder
add_action_files(
  FILES Pose.action
)
## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES actionlib_msgs geometry_msgs std_msgs
)
###################################
## catkin specific configuration ##
###################################
## CATKIN_DEPENDS: catkin_packages dependent projects also need
catkin_package(
  CATKIN_DEPENDS roscpp rospy message_runtime actionlib_msgs geometry_msgs std_msgs
)
###########
## Build ##
###########
## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)
