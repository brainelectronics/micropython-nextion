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

# ============================================================================
# ============================== Example values ==============================
# new values of waveform
background_color_value = 63488  # red

# ============================================================================
# ============================ Datapoint functions ===========================
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

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of waveform "s0"
print('Requesting background color of waveform "{}" ...'.format(s0.name))
response = s0.Get_background_color_bco()
print('Background color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

time.sleep(1)

# modify the background color of waveform "s0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of waveform "{}" to "{}"'.
      format(s0.name, background_color_value))
s0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of waveform "s0" again
print('Requesting background color of waveform "{}" ...'.format(s0.name))
response = s0.Get_background_color_bco()
print('Background color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
