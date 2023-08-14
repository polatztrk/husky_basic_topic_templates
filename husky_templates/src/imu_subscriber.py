#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

def imu_callback(data):

    rospy.loginfo("Recieved IMU data \n%s",data)

def imu_subscriber():

    rospy.init_node('imu_subscriber',anonymous=True)

    rospy.Subscriber("/imu/data",Imu, imu_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        imu_subscriber()
    except rospy.ROSInterruptException:
        pass
