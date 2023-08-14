#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def cmd_vel_input(x_vel):
    msg=Twist()
    msg.linear.x=float(x_vel)
    pub.publish(msg)
    print("Published")

#For rotation move you can use this function instead of upper one:
"""
def cmd_vel_input(x_vel):
    msg=Twist()
    msg.linear.z=float(x_vel)
    pub.publish(msg)
    print("Published")
"""
if __name__ == '__main__':
    print("Running")
    rospy.init_node('go_husky', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    while not rospy.is_shutdown():
        r=rospy.Rate(10)
        velocity=input("Please Enter a Velocity Value in x Direction. Between -1 and 1")
        cmd_vel_input(velocity)
        r.sleep()

