#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a waveform element
"""

# system packages
import time

# custom packages
from nextion import NexWaveform, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a waveform instance (CID is 14, see HMI file)
s0 = NexWaveform(nh, 0, 14, "s0")

# modify waveform "s0"
print('Add datapoints to waveform "{}"'.format(s0.name))
for x in range(0, 100):
    channel_0_value = x
    channel_1_value = 100 - x
    channel_2_value = 20
    channel_3_value = int(x / 2)
    s0.addValue(0, channel_0_value)
    s0.addValue(1, channel_1_value)
    s0.addValue(2, channel_2_value)
    s0.addValue(3, channel_3_value)
    time.sleep(0.1)
print()

time.sleep(1)

# remove channel 0 waveform
print('Removing channel 0 waveform...')
s0.clearChannel(0)
print()

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
