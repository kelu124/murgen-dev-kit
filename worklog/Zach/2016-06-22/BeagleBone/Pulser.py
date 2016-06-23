# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:34:05 2016

@author: OptLab
"""

import Adafruit_BBIO.PWM as pwm
pos = "P9_22"
neg = "P9_21"
pwm.stop(pos)
pwm.stop(neg)
pwm.start(pos,(100 - 5e-6),20,1)
pwm.stop(pos)
pwm.start(pos,(100 - 5e-6),20,1)
pwm.stop(pos)
pwm.start(pos,(100 - 5e-6),20,1)
pwm.stop(pos)
pwm.start(neg,(5e-6),20,0)
