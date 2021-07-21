#!/usr/bin/env python
import rospy
from std_msgs.msg import String
comb_msg= "" 
def callback(data):
     global comb_msg
     comb_msg= comb_msg + data.data
     #rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
     
def listener():
 
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('listener', anonymous=True)
     rospy.Subscriber("/world", String, callback)
     rospy.Subscriber("/hello", String, callback)
     
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()
def talker():
     global comb_msg
     pub = rospy.Publisher('/helloworld', String, queue_size=10)
     #rospy.init_node('talker3', anonymous=True)
     rate = rospy.Rate(10) # 10hz
     while not rospy.is_shutdown():
         hello_str = comb_msg+("%s" % rospy.get_time())
         comb_msg=""
         rospy.loginfo(hello_str)
         pub.publish(hello_str)
         rate.sleep()     
 
if __name__ == '__main__':
     listener()
