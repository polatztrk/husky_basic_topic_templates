#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix

def callback(data):
    rospy.loginfo("Received GPS Fix:")
    rospy.loginfo("Latitude: %f", data.latitude)
    rospy.loginfo("Longitude: %f", data.longitude)
    rospy.loginfo("Altitude: %f", data.altitude)

def gps_subscriber_node():
    # Initialize the ROS node
    rospy.init_node('gps_subscriber', anonymous=True)

    # Subscribe to the "/fix" topic with NavSatFix messages
    rospy.Subscriber('/fix', NavSatFix, callback)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        gps_subscriber_node()
    except rospy.ROSInterruptException:
        pass

