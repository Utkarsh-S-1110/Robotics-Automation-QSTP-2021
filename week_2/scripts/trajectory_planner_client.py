#!/usr/bin/env python
 
from __future__ import print_function
 
import sys
import numpy as np
import rospy
from week_2.srv import *
 
def trajectory_planner_client():
   rospy.wait_for_service('trajectory_planner')
   x=0.0
   y=0.0
   theta=0.0
   v=1.0
   w=0.5
   dt=0.05
   n=50
   to_radian=np.pi/180
   theta/=to_radian
   for i in range(n):
      try:
         trajectory_planner = rospy.ServiceProxy('trajectory_planner', Trajectory_Planner)
         theta_temp=theta
         x+=((v/w)*(np.sin((theta_temp*to_radian)+(w*dt))-np.sin((theta_temp*to_radian))))
         y+=((v/w)*(np.cos((theta_temp*to_radian))-np.cos((theta_temp*to_radian)+(w*dt))))
         theta=(theta_temp+(w*dt/to_radian))
         resp1 = trajectory_planner(x, y)
         
      except rospy.ServiceException as e:
         print("Service call failed: %s"%e)
   return resp1.sum 	
 
def usage():
   return "%s [x y]"%sys.argv[0]
 
if __name__ == "__main__":
   trajectory_planner_client()
