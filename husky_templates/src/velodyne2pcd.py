#!/usr/bin/env python3

import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import numpy as np
import open3d as o3d

def velodyne_callback(msg):
    # Convert ROS PointCloud2 message to numpy array
    pc_data = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
    points = np.array(list(pc_data))

    # Create an Open3D PointCloud object
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points[:, :3])

    # Save PCD file using Open3D
    o3d.io.write_point_cloud('output.pcd', point_cloud)
    rospy.loginfo('PCD file saved.')

if __name__ == '__main__':
    rospy.init_node('velodyne_pcd_saver')
    rospy.Subscriber('/velodyne_points', PointCloud2, velodyne_callback)
    rospy.spin()
