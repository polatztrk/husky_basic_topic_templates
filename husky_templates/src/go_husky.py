#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback():
    r = rospy.Rate(10)
    def forward():
        msg=Twist()
        msg.linear.x=0.5
        return msg
    def backward():
        msg=Twist()
        msg.linear.x=-0.5
        return msg
    def left():
        msg=Twist()
        msg.angular.z=0.7
        return msg
    def right():
        msg=Twist()
        msg.angular.z=-0.7
        return msg
    
    global msg
    count1 = 0
    while(count1<20):
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        msg1=Twist()
        msg1=forward()
        pub.publish(msg1)
        print("Publishing...")
        count1=count1+1
        r.sleep()
    count2=0
    while(count2<20):
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        msg1=Twist()
        msg1=left()
        pub.publish(msg1)
        print("Publishing...")
        count2=count2+1 
        r.sleep()

    count3 = 0
    while(count3<20):
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        msg1=Twist()
        msg1=forward()
        pub.publish(msg1)
        print("Publishing...")
        count3=count3+1
        r.sleep()      
    #while not rospy.is_shutdown():
        #pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        #pub.publish(msg)
        #print("Publishing...")
        #r.sleep()

if __name__ =='__main__':
    print("Running")
    rospy.init_node('go_husky', anonymous=True)
    callback()

