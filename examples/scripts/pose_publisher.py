#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose

rospy.init_node('pose_publisher')

pub = rospy.Publisher('pose', Pose, queue_size=10)

rate = rospy.Rate(10)

pose = Pose()

while not rospy.is_shutdown():
    pub.publish(pose)
    pose.position.z += 1
    rate.sleep()
