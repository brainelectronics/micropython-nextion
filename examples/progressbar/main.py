#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a progressbar element
"""

# system packages
from random import choice, randint
import time

# custom packages
from nextion import NexHardware, NexProgressBar

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a progressbar instance
j0 = NexProgressBar(nh, 0, 1, "j0")

# new value of progressbar, avoid something close to zero or close to 50
progressbar_value = choice([randint(5, 40), randint(60, 100)])

# request the value of progressbar "j0" being 50 by default
print('Requesting progressbar "{}" value ...'.format(j0.name))
response = j0.getValue()
print('Progressbar "{}" value is: "{}"'.format(j0.name, response))
print()

time.sleep(1)

# modify progressbar "j0" being checked by default
print('Set progressbar "{}" to "{}"'.format(j0.name, progressbar_value))
j0.setValue(progressbar_value)
print()

time.sleep(1)

# request the value of progressbar "j0" again
print('Requesting progressbar "{}" value ...'.format(j0.name))
response = j0.getValue()
print('Progressbar "{}" value is: "{}"'.format(j0.name, response))
print()

# sanity check
if response != progressbar_value:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
