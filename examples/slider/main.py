#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a slider element
"""

# system packages
from random import choice, randint
import time

# custom packages
from nextion import NexSlider, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a slider instance
h0 = NexSlider(nh, 0, 1, "h0")

# new value of slider, avoid something close to zero or close to 50
slider_value = choice([randint(5, 40), randint(60, 100)])

# request the value of slider "h0"
print('Requesting slider "{}" value ...'.format(h0.name))
response = h0.getValue()
print('Slider "{}" value is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify slider "h0" showing "50" by default
print('Set slider "{}" to "{}"'.format(h0.name, slider_value))
h0.setValue(slider_value)
print()

time.sleep(1)

# request the value of slider "h0" again
print('Requesting slider "{}" value ...'.format(h0.name))
response = h0.getValue()
print('slider "{}" value is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != slider_value:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
