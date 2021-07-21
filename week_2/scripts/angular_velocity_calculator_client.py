#!/usr/bin/env python
 
from __future__ import print_function
 
import sys
from week_2.msg import SingleMsg
import rospy
from week_2.srv import *
 
radius=1.0
angularVel=0.0

def angular_velocity_calculator_client():
   global radius,angularVel
   rospy.wait_for_service('compute_ang_vel')
   try:
      angular_velocity_calculator = rospy.ServiceProxy('compute_ang_vel', AngularVelocityCalculator)
      resp1 = angular_velocity_calculator(radius)
      angularVel= resp1.ang_vel
   except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
   try:
      talker()
   except rospy.ROSInterruptException:
      pass   
 
def usage():
   return "%s [x y]"%sys.argv[0]
 
def callback(data):
     global radius
     radius= data.single_msg
     #rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
     
def listener():
   rospy.init_node('listener', anonymous=True)
   rospy.Subscriber("/radius", SingleMsg, callback)
   try:
      angular_velocity_calculator_client()
   except rospy.ROSInterruptException:
      pass
     # spin() simply keeps python from exiting until this node is stopped
   rospy.spin()

def talker():
   pub = rospy.Publisher('/cmd_vel', SingleMsg, queue_size=10)
   #rospy.init_node('talker2', anonymous=True)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():
      global angularVel
      msg=SingleMsg()
      msg.single_msg=angularVel
      rospy.loginfo(msg)
      pub.publish(msg)
      rate.sleep()

if __name__ == "__main__":
   listener()    
