#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from examples.srv import PoseAdd, PoseAddResponse

def callback(req):
    c = Pose()
    c.position.z = req.a.position.z + req.b.position.z
    return PoseAddResponse(c)

rospy.init_node('pose_service_server')

service = rospy.Service('pose_add', PoseAdd, callback)

rospy.spin()
