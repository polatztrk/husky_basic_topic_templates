#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

def imu_callback(data):

    
    linear_acc_x=data.linear_acceleration.x
    linear_acc_y=data.linear_acceleration.y
    linear_acc_z=data.linear_acceleration.z

    rospy.loginfo("Recieved IMU data (x,y,z): %.4f,%.4f,%.4f",linear_acc_x,linear_acc_y,linear_acc_z)

def imu_subscriber():

    rospy.init_node('imu_subscriber',anonymous=True)

    rospy.Subscriber("/imu/data",Imu, imu_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        imu_subscriber()
    except rospy.ROSInterruptException:
        pass
