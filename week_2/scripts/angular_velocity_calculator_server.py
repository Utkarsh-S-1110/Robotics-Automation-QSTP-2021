#!/usr/bin/env python


from __future__ import print_function
from std_msgs.msg import String
from week_2.srv import AngularVelocityCalculator,AngularVelocityCalculatorResponse
import rospy

 
def handle_angular_velocity_calculator(req):
    return AngularVelocityCalculatorResponse(0.1/req.radius)
 
def angular_velocity_calculator():
    rospy.init_node('angular_velocity_calculator_server')
    s = rospy.Service('compute_ang_vel', AngularVelocityCalculator, handle_angular_velocity_calculator)
    print("Ready to calculate angular velocity.")
    rospy.spin()
 
if __name__ == "__main__":
    angular_velocity_calculator()
