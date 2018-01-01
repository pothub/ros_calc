#!/usr/bin/env python

import rospy
# import original message type CalcElement
from calc.msg import CalcElement
# import message type Int32
from std_msgs.msg import Int32

rospy.init_node('calculation')
# Arg 1 is publish topic name, arg 2 is publish data type
pub = rospy.Publisher('CalcAnser', Int32)

def callback(msg):
    if msg.ope == "+":
        ans = msg.a + msg.b
    if msg.ope == "-":
        ans = msg.a - msg.b
    if msg.ope == "*":
        ans = msg.a * msg.b
    if msg.ope == "/":
        ans = msg.a / msg.b
    pub.publish(ans)

sub = rospy.Subscriber('CalcElement', CalcElement, callback)
# while(!this node shutdown); 
rospy.spin()

