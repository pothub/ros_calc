#!/usr/bin/env python

import rospy
# import original message type CalcElement
from calc.msg import CalcElement

rospy.init_node('input')
# Arg 1 is publish topic name, arg 2 is publish data type
pub = rospy.Publisher('CalcElement', CalcElement)

while not rospy.is_shutdown():
    msg = CalcElement()
    CalcElementList = raw_input().split()
    msg.a = int(CalcElementList[0])
    msg.ope = CalcElementList[1]
    msg.b = int(CalcElementList[2])

    pub.publish(msg)

