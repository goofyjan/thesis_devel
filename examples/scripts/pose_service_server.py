#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from examples.srv import PoseAdd, PoseAddResponse

def callback(req):
    a = req.a.position.z
    b = req.b.position.z
    c = Pose()
    c.position.z = a + b
    return PoseAddResponse(c)

rospy.init_node('pose_service_server')

service = rospy.Service('pose_add', PoseAdd, callback)

rospy.spin()
