#!/usr/bin/env python
import rospy
import copy
import time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('open_gripper')

pub = rospy.Publisher('gripper_controller/command', JointTrajectory, queue_size=10)

trajectory = JointTrajectory()
points = JointTrajectoryPoint()

trajectory.joint_names.append("r_finger_joint")
trajectory.joint_names.append("l_finger_joint")
points.positions = [0.0,0.0]
points.time_from_start.secs = 1.0

trajectory.points.append(points)
rate = rospy.Rate(10);

while not rospy.is_shutdown():
     pub.publish(trajectory)
     rate.sleep()

rospy.spin()
