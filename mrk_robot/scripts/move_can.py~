#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import shape_msgs.msg 
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_test', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")
# group.allow_replanning(True)
# group.set_goal_joint_tolerance(2.0)
# group.set_goal_orientation_tolerance(2.0)
# group.set_goal_position_tolerance(2.0)
# group.set_num_planning_attempts(3)
# group.set_planning_time(40)
# group.set_pose_reference_frame("world")
pose_target = Pose()
robot.get_current_state

rospy.sleep(1)
# group.set_named_target("up")
# group.go(wait=True)

# pose_target.orientation = Quaternion(*quaternion_from_euler(3.1416, 0.0, -1.5708))
# pose_target.position.x = -0.4
# pose_target.position.y = -0.5
# pose_target.position.z = 1.3
# group.set_pose_target(pose_target)
# group.go(wait=True)
# rospy.sleep(5)

pose_target.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, -1.5708))
pose_target.position.x = 0.4
pose_target.position.y = -0.47
pose_target.position.z = 1.3
group.set_pose_target(pose_target)
group.go(wait=True)

pose_target.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, -1.5708))
pose_target.position.x = 0.4
pose_target.position.y = -0.47
pose_target.position.z = 1.2
group.set_pose_target(pose_target)
group.go(wait=True)

moveit_commander.roscpp_shutdown()

