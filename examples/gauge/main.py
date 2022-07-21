#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a gauge element
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexGauge, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a gauge instance
z0 = NexGauge(nh, 0, 1, "z0")

# new value of gauge
gauge_value = randint(10, 350)

# request the value of gauge "z0"
print('Requesting gauge "{}" value ...'.format(z0.name))
response = z0.getValue()
print('Gauge "{}" value is: "{}"'.format(z0.name, response))
print()

time.sleep(1)

# modify gauge "z0" being checked by default
print('Set gauge "{}" to "{}"'.format(z0.name, gauge_value))
z0.setValue(gauge_value)
print()

time.sleep(1)

# request the value of gauge "z0" again
print('Requesting gauge "{}" value ...'.format(z0.name))
response = z0.getValue()
print('Gauge "{}" value is: "{}"'.format(z0.name, response))
print()

# sanity check
if response != gauge_value:
    print('WARNING: GET value did not match SET value')

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
