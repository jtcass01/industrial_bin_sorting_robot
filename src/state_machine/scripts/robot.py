#!/usr/bin/env python

import enum

class ROBOT_STATES(enum.Enum):
    PICKING_UP = 'picking_up'
    PLACING = 'placing'
    RETURNING_TO_WAIT = 'returning_to_wait'
    WAITING = 'waiting'
