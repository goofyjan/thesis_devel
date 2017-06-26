#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose

def callback(msg):
    print msg
    
rospy.init_node('pose_subscriber')

sub = rospy.Subscriber('pose', Pose, callback)

rospy.spin()
