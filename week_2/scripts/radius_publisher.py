#!/usr/bin/env python
# license removed for brevity
import rospy
from week_2.msg import SingleMsg
 
def talker():
    radius=1.0
    pub = rospy.Publisher('/radius',SingleMsg, queue_size=10)
    rospy.init_node('radius_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg=SingleMsg()
        msg.single_msg=radius
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass




