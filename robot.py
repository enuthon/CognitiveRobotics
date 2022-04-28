#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
x = ""

def callback(data):
    control(data.data)
    
def control(x):
    print(x)
    if(x == "forward"):
        rbts.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    elif(x == "left"):
        rbts.turn_in_place(degrees(90)).wait_for_completed()
    elif (x == "right"):
        rbts.turn_in_place(degrees(-90)).wait_for_completed()
    	
def main(rbt: cozmo.robot.Robot):
    global rbts
    rbts = rbt
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('recognition', String, callback)
    rospy.spin()


if __name__ == '__main__':
    cozmo.run_program(main)
