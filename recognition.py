#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def main():
    I = input("something to send: ")
    send(I)

def send(message):
    pub = rospy.Publisher('recognition', String, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    rospy.loginfo(message)
    pub.publish(message)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
