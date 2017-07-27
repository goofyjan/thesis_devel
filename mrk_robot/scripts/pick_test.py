#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import shape_msgs.msg 
from geometry_msgs.msg import Pose, PoseStamped, PoseArray, Quaternion
from tf.transformations import quaternion_from_euler

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")

robot.get_current_state

rospy.sleep(1)

# clean the scene
scene.remove_world_object("pole")
scene.remove_world_object("table")
scene.remove_world_object("part")

# publish a demo scene
p = PoseStamped()
p.header.frame_id = robot.get_planning_frame()
# p.pose.position.x = 0.7
# p.pose.position.y = -0.4
# p.pose.position.z = 0.85
# p.pose.orientation.w = 1.0
# scene.add_box("pole", p, (0.3, 0.1, 1.0))

p.pose.position.x = 0.0
p.pose.position.y = -0.7
p.pose.position.z = 0.5
scene.add_box("table", p, (2.0, 1.0, 0.01))

p.pose.position.x = -0.1
p.pose.position.y = -0.5
p.pose.position.z = 1.3
scene.add_box("part", p, (0.03, 0.03, 0.03))

rospy.sleep(1)

robot.arm.pick("part")


rospy.spin()
moveit_commander.roscpp_shutdown()
roscpp_shutdown()
