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

# ============================================================================
# ============================== Example values ==============================
# new values of radio
radio_state = 0
background_color_value = 63488  # red
font_color_value = 31           # blue

# ============================================================================
# ============================== Value functions =============================
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

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of radio "r0"
print('Requesting background color of radio "{}" ...'.format(r0.name))
response = r0.Get_background_color_bco()
print('Background color of radio "{}" is: "{}"'.format(r0.name, response))
print()

time.sleep(1)

# modify the background color of radio "r0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of radio "{}" to "{}"'.
      format(r0.name, background_color_value))
r0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of radio "r0" again
print('Requesting background color of radio "{}" ...'.format(r0.name))
response = r0.Get_background_color_bco()
print('Background color of radio "{}" is: "{}"'.format(r0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of radio "r0"
print('Requesting font color of radio "{}" ...'.format(r0.name))
response = r0.Get_font_color_pco()
print('Font color of radio "{}" is: "{}"'.format(r0.name, response))
print()

time.sleep(1)

# enable radio "r0" again to make change in font color visible
r0.setValue(1)

# modify the font color of radio "r0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of radio "{}" to "{}"'.
      format(r0.name, font_color_value))
r0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of radio "r0" again
print('Requesting font color of radio "{}" ...'.format(r0.name))
response = r0.Get_font_color_pco()
print('Font color of radio "{}" is: "{}"'.format(r0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
