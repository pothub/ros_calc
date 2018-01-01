#!/usr/bin/env python

import rospy
# import message type Int32
from std_msgs.msg import Int32

rospy.init_node('output')

def callback(msg):
    print 'ans', msg

sub = rospy.Subscriber('CalcAnser', Int32, callback)
# while(!this node shutdown); 
rospy.spin()

