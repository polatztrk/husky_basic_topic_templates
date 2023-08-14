#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion

def imu_callback(data):

    orientation_quater=data.orientation
    (roll,pitch,yaw)=euler_from_quaternion([orientation_quater.x,orientation_quater.y,orientation_quater.z,orientation_quater.w])
    rospy.loginfo("Orientation (Roll,Pitch,Yaw): %.4f, %.4f,%.4f",roll,pitch,yaw)

def imu_subscriber():

    rospy.init_node('imu_subscriber',anonymous=True)

    rospy.Subscriber("/imu/data",Imu, imu_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        imu_subscriber()
    except rospy.ROSInterruptException:
        pass