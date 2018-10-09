#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from robot import ROBOT_STATES


def update_state():
    robot_state_index = 0
    robot_states = [ROBOT_STATES.PICKING_UP, ROBOT_STATES.PLACING, ROBOT_STATES.RETURNING_TO_WAIT, ROBOT_STATES.WAITING]

    pub = rospy.Publisher('robot_state', String, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(1) #1Hz
    while not rospy.is_shutdown():
	# DECIDE ROBOT STATE HERE.

	# SET ROBOT STATE
        robot_state = robot_states[robot_state_index % len(robot_states)]

	# PUBLISH NEW STATE FROM THE CONTROLLER TO THE ENVIRONMENT
        rospy.loginfo(robot_state)
        pub.publish(robot_state.value)
        robot_state_index += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        update_state()
    except rospy.ROSInterruptException:
        pass
