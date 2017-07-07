#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import shape_msgs.msg 
from geometry_msgs.msg import Pose, PoseStamped, PoseArray, Quaternion
from tf.transformations import quaternion_from_euler

print "============ Starting tutorial setup"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")

# print "============ Reference frame: %s" % group.get_planning_frame()
# print "============ Reference frame: %s" % group.get_end_effector_link()
# print "============ Robot Groups:"
# print robot.get_group_names()
# print "============ Printing robot state"
# print robot.get_current_state()
# print "============"

# print "============ Generating plan 1"

robot.get_current_state
pose_target = Pose()
group.clear_pose_targets()
# pose_target.orientation.w = 0.0
# pose_target.position.x = -0.7
# pose_target.position.y = -0.3
# pose_target.position.z = 1.1
# group.set_pose_target(pose_target)
# group.go(wait=True)
# rospy.sleep(5)

pose_target.orientation = Quaternion(*quaternion_from_euler(90.0, 0.0, 0.0))
pose_target.position.x = -0.65
pose_target.position.y = -0.3
pose_target.position.z = 1.3
group.set_pose_target(pose_target)
group.go(wait=True)
rospy.sleep(5)

pose_target.orientation = Quaternion(*quaternion_from_euler(90.0, 0.0, 0.0))
pose_target.position.x = 0.65
pose_target.position.y = -0.3
pose_target.position.z = 1.3
group.set_pose_target(pose_target)
group.go(wait=True)
rospy.sleep(5)

pose_target.orientation = Quaternion(*quaternion_from_euler(90.0, 0.0, 0.0))
pose_target.position.x = 0.3
pose_target.position.y = -0.3
pose_target.position.z = 1.3
group.set_pose_target(pose_target)
group.go(wait=True)
rospy.sleep(5)

# group.clear_pose_targets()
# group.set_named_target("place")
# group.go(wait=True)
# rospy.sleep(5)
# group.set_named_target("up")
# group.go(wait=True)
# rospy.sleep(5)
# group.set_named_target("home")
# group.go(wait=True)

# plan1 = group.plan()

# group.execute(plan1)

moveit_commander.roscpp_shutdown()
