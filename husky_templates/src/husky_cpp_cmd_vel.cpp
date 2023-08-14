#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <iostream>

void cmd_vel_input(float x_vel){

}

int main(int argc, char **argv){

    ros::init(argc,argv,"cmd_vel_publisher");

    ros::NodeHandle nh;

    ros::Publisher cmd_vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel",10);

    ros::Rate loop_rate(10);
    while(ros::ok()){
        float velocity;
        std::cout<<"Please Enter a Velocity Value in x Direction. Between -1 and 1";
        std::cin>> velocity;
        geometry_msgs::Twist msg;
        msg.linear.x = velocity;
        cmd_vel_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}