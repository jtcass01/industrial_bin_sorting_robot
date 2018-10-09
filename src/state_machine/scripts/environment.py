#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from robot import ROBOT_STATES

def update_robot_state(data):
    # Retrieve ROBOT_STATE FROM data as it relates to ROBOT_STATES enum
    robot_state = ROBOT_STATES(data.data)

    # DO WORK WITH STATE USING THE FOLLOWING DICTIONARY OF FUNCTIONS
    switcher = {
        ROBOT_STATES.WAITING : wait,
        ROBOT_STATES.PICKING_UP : pick_up,
        ROBOT_STATES.PLACING : place,
        ROBOT_STATES.RETURNING_TO_WAIT : return_to_wait
    }
    robo_func = switcher.get(robot_state, "invalid robot_state")

    # Execute the state function.  Can take additional arguments
    robo_func()

    # LOG STATE
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(robot_state))


def return_to_wait():
    print("Returning to wait - func")
    pass

def wait():
    print("wait - func")
    pass

def pick_up():
    print("picking_up - func")
    pass

def place():
    print("placing - func")
    pass

def listener():
    rospy.init_node('environment', anonymous=True)
    rospy.Subscriber('robot_state', String, update_robot_state)

    rospy.spin()

if __name__ == '__main__':
    listener()
