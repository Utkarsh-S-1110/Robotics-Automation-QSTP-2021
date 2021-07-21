#!/usr/bin/env python
 
from __future__ import print_function
 
from week_2.srv import Trajectory_Planner,Trajectory_PlannerResponse
import rospy
 
def handle_trajectory_planner(req):
    print("Plotting [%s, %s]"%(req.x, req.y))
    return Trajectory_PlannerResponse(req.x + req.y)
 
def trajectory_planner():
    rospy.init_node('trajectory_planner_server')
    s = rospy.Service('trajectory_planner', Trajectory_Planner, handle_trajectory_planner)
    print("Ready to plot.")
    rospy.spin()
 
if __name__ == "__main__":
    trajectory_planner()
