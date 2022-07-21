#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a radio element
"""

# system packages
import time

# custom packages
from nextion import NexRadio, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a radio instance
r0 = NexRadio(nh, 0, 1, "r0")

# new state of radio
radio_state = 0

# request the state of radio "r0"
print('Requesting radio "{}" value ...'.format(r0.name))
response = r0.getValue()
print('Radio "{}" value is: "{}"'.format(r0.name, response))
print()

time.sleep(1)

# modify radio "r0" being enabled by default
print('Set radio "{}" to "{}"'.format(r0.name, radio_state))
r0.setValue(radio_state)
print()

time.sleep(1)

# request the state of radio "r0" again
print('Requesting radio "{}" value ...'.format(r0.name))
response = r0.getValue()
print('Radio "{}" value is: "{}"'.format(r0.name, response))
print()

# sanity check
if response != radio_state:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
