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
grid_color_value = 31           # blue
grid_width = 20
grid_height = 20
channel_0_color = 64480         # orange

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
# ============================ Special functions =============================
# ============================================================================
# =========================== Grid color functions ===========================
# request the grid color of waveform "s0"
print('Requesting grid color of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_color_gdc()
print('Grid color color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

time.sleep(1)

# modify the grid color of waveform "s0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set grid color of waveform "{}" to "{}"'.
      format(s0.name, grid_color_value))
s0.Set_grid_color_gdc(grid_color_value)
print()

time.sleep(1)

# request the grid color of waveform "s0" again
print('Requesting grid color of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_color_gdc()
print('Grid color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

# sanity check
if response != grid_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ========================= Channel color functions ==========================
# request the channel 0 color of waveform "s0"
print('Requesting channel 0 color of waveform "{}" ...'.format(s0.name))
response = s0.Get_channel_0_color_pco0()
print('Channel 0 color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

time.sleep(1)

# modify the channel 0 color of waveform "s0" to "orange"
# search for RGB565 Colors. Orange is "64480" at 65k colors
print('Set channel 0 color of waveform "{}" to "{}"'.
      format(s0.name, channel_0_color))
s0.Set_channel_0_color_pco0(channel_0_color)
print()

time.sleep(1)

# request the channel 0 color of waveform "s0" again
print('Requesting channel 0 color of waveform "{}" ...'.format(s0.name))
response = s0.Get_channel_0_color_pco0()
print('Channel 0 color of waveform "{}" is: "{}"'.format(s0.name, response))
print()

# sanity check
if response != channel_0_color:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ========================= Grid dimenstion functions ========================
# request the grid width of waveform "s0"
print('Requesting grid width of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_width_gdw()
print('Grid width of waveform "{}" is: "{}"'.format(s0.name, response))
print()

time.sleep(1)

# modify the grid width of waveform "s0"
print('Set grid width of waveform "{}" to "{}"'.format(s0.name, grid_width))
s0.Set_grid_width_gdw(grid_width)
print()

time.sleep(1)

# request the grid width of waveform "s0" again
print('Requesting grid width of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_width_gdw()
print('Grid width of waveform "{}" is: "{}"'.format(s0.name, response))
print()

# sanity check
if response != grid_width:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the grid height of waveform "s0"
print('Requesting grid height of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_height_gdh()
print('Grid height of waveform "{}" is: "{}"'.format(s0.name, response))
print()

time.sleep(1)

# modify the grid height of waveform "s0"
print('Set grid height of waveform "{}" to "{}"'.format(s0.name, grid_height))
s0.Set_grid_height_gdh(grid_height)
print()

time.sleep(1)

# request the grid height of waveform "s0" again
print('Requesting grid height of waveform "{}" ...'.format(s0.name))
response = s0.Get_grid_height_gdh()
print('Grid height of waveform "{}" is: "{}"'.format(s0.name, response))
print()

# sanity check
if response != grid_height:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
