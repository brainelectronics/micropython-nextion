#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a number element
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexNumber, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a number instance
n0 = NexNumber(nh, 0, 1, "n0")

# new value of number field
number_value = randint(1, 100)

# request the value of number "n0"
print('Requesting number "{}" value ...'.format(n0.name))
response = n0.getValue()
print('Number field "{}" value is: "{}"'.format(n0.name, response))
print()

time.sleep(1)

# modify number field "n0" showing "0" by default
print('Set number field "{}" to "{}"'.format(n0.name, number_value))
n0.setValue(number_value)
print()

time.sleep(1)

# request the value of number "n0" again
print('Requesting number "{}" value ...'.format(n0.name))
response = n0.getValue()
print('Number field "{}" value is: "{}"'.format(n0.name, response))
print()

# sanity check
if response != number_value:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
