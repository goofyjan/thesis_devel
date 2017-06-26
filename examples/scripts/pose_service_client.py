#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from examples.srv import PoseAdd

rospy.init_node('pose_service_client')

rospy.wait_for_service('pose_add')

srv = rospy.ServiceProxy('pose_add', PoseAdd)

pose1 = Pose()
pose1.position.z = 1
pose2 = Pose()
pose2.position.z = 2
resp = srv(pose1, pose2)

print resp.sum
