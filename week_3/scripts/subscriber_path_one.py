#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Twist
from tf.transformations import euler_from_quaternion
import math 
import time

class PlanPath:
     def __init__(self):
          self.theta=0.0
          self.recieved=0
          self.cnt=0

     def callback(self,data):
          while self.recieved < 1:
               print("Ready to start callback function")
               pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
               rot=Twist()
               rate = rospy.Rate(10)
               length= len(data.poses)
               sub = rospy.Subscriber("/odom", Odometry, self.newOdom)
               
               for i in range(1,length):
                    current_x=0
                    current_y=0
                    if i>1:
                        current_x=data.poses[i-1].pose.position.x
                        current_y=data.poses[i-1].pose.position.y
                    
                    target_x= data.poses[i].pose.position.x
                    target_y= data.poses[i].pose.position.y
                    inc_x = target_x -current_x
                    inc_y = target_y -current_y
                    distance = math.sqrt((inc_x*inc_x)+(inc_y*inc_y))
                    time_to_distance=distance/0.10
                    angle_to_goal = math.atan2(inc_y, inc_x) 
                    print("Ready to enter while loop")
                    while abs(angle_to_goal - self.theta) > 0.1:
                         sub = rospy.Subscriber ('/odom', Odometry, self.newOdom)
                         rot=Twist()
                         rot.linear.x= 0.0
                         rot.angular.z=0.5*(angle_to_goal - self.theta)
                         rospy.loginfo(rot)
                         pub.publish(rot) 
                         sub.unregister()
                         rate.sleep() 
                    print("Facing Destination") 
                    rot.linear.x=0.1
                    rot.angular.z=0.0
                    rospy.loginfo(rot)
                    pub.publish(rot)
                    time.sleep(time_to_distance)  
                    print("Reached destination")     
                    rot.linear.x=0.0
                    rot.angular.z=0.0
                    rospy.loginfo(rot)
                    pub.publish(rot)
               self.recieved+=1     

     
     def listener(self):
             
         topic="/path3"                                                # Determines topic to be used
         print("Attempt %d",self.cnt) 
         rospy.init_node('listener_path1', anonymous=True)
         print("Initiated")
         rospy.Subscriber(topic, Path, self.callback)
         pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
         rot=Twist()
         rate = rospy.Rate(10)
         
         if topic=='/path3':                      # The robot was not executing the first step from the for loop, so had to hardcode it.     
             angle_to_goal = math.atan2(3, 1) 
             print("Ready to enter while loop")
             while abs(angle_to_goal - self.theta) > 0.1:
                 sub = rospy.Subscriber ('/odom', Odometry, self.newOdom)
                 rot=Twist()
                 rot.linear.x= 0.0
                 rot.angular.z=0.5*(angle_to_goal - self.theta)
                 rospy.loginfo(rot)
                 pub.publish(rot) 
                 sub.unregister()
                 rate.sleep() 
             print("Facing Destination") 
             rot.linear.x=0.1
             rot.angular.z=0.0
             rospy.loginfo(rot)
             pub.publish(rot)
             time.sleep(31.6227766)  
             print("Reached destination")     
             rot.linear.x=0.0
             rot.angular.z=0.0
             rospy.loginfo(rot)
             pub.publish(rot)


         elif (topic=='/path1') or (topic=='/path2'):
             print("Topic 1/2 is being used")
             rot.linear.x=0.1
             rot.angular.z=0.0
             rospy.loginfo(rot)
             pub.publish(rot)
             time.sleep(30)  
             rot.linear.x=0.0
             rot.angular.z=0.0
             rospy.loginfo(rot)
             pub.publish(rot)
             
         
         while not (self.recieved):
             self.cnt+=1
             rospy.spin()

     def newOdom(self,msg):
          self.theta
          rot_q = msg.pose.pose.orientation
          (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
 
if __name__ == '__main__':
     obj=PlanPath()
     obj.listener()
