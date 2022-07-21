#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a checkbox element
"""

# system packages
import time

# custom packages
from nextion import NexCheckbox, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a checkbox instance
c0 = NexCheckbox(nh, 0, 1, "c0")

# new value of checkbox
checkbox_value = 0

# request the value of checkbox "c0"
print('Requesting checkbox "{}" value ...'.format(c0.name))
response = c0.getValue()
print('checkbox "{}" value is: "{}"'.format(c0.name, response))
print()

time.sleep(1)

# modify checkbox "c0" being checked by default
print('Set checkbox "{}" to "{}"'.format(c0.name, checkbox_value))
c0.setValue(checkbox_value)
print()

time.sleep(1)

# request the value of checkbox "c0" again
print('Requesting checkbox "{}" value ...'.format(c0.name))
response = c0.getValue()
print('checkbox "{}" value is: "{}"'.format(c0.name, response))
print()

# sanity check
if response != checkbox_value:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
