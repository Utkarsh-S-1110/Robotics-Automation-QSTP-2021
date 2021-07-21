#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import Twist
clockwise=True 
def talker():
    global clockwise
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.init_node('path_instructor', anonymous=True)
    rot=Twist()
    rot.linear.x=0.22
    rot.angular.z=0.4
    rospy.loginfo(rot)
    pub.publish(rot)
    rate = rospy.Rate(0.4/(2* math.pi))
    while not rospy.is_shutdown():
        clockwise=not clockwise
        
        if clockwise:
            rot.linear.x=0.22
            rot.angular.z=0.4
        else : 
            rot.linear.x=0.22
            rot.angular.z= -(0.4)            
        rospy.loginfo(rot)
        pub.publish(rot)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
