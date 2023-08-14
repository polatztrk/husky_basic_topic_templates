#include <iostream>
#include <ros/ros.h>
#include <gps_common/GPSFix.h>

class GpsTest
{
public:
    gps_common::GPSFix gpsMsg;

    GpsTest(ros::NodeHandle nh_) : n(nh_)
    {
        gps_sub = n.subscribe("/fix",100,&GpsTest::gpsCallback,this);
    }

    void gpsCallback(const gps_common::GPSFixConstPtr &msg){
        gpsMsg = *msg;
    }

private:
    ros::NodeHandle n;

    ros::Subscriber gps_sub;
};

int main(int argc, char** argv)
{
    double gpsLat = 0;
    double gpsLong = 0;

    ros::init(argc,argv,"gps_Subscriber");
    ros::NodeHandle nh_;

    GpsTest *p = new GpsTest(nh_);

    gpsLong = p->gpsMsg.longitude;
    gpsLat = p->gpsMsg.latitude;

    std::cout<<"Current Longitude: "<<gpsLat<<std::endl;
    std::cout<<"Current Latitude: "<<gpsLong<<std::endl;

    ros::spin();
    return 0;
}
