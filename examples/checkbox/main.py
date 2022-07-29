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

# new values of checkbox
checkbox_value = 0
background_color_value = 63488  # red
font_color_value = 31           # blue

# request the value of checkbox "c0"
print('Requesting checkbox "{}" value ...'.format(c0.name))
response = c0.getValue()
print('Checkbox "{}" value is: "{}"'.format(c0.name, response))
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
print('Checkbox "{}" value is: "{}"'.format(c0.name, response))
print()

# sanity check
if response != checkbox_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the background color of checkbox "c0"
print('Requesting background color of checkbox "{}" ...'.format(c0.name))
response = c0.Get_background_color_bco()
print('Background color of checkbox "{}" is: "{}"'.format(c0.name, response))
print()

time.sleep(1)

# modify the background color of checkbox "c0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of checkbox "{}" to "{}"'.
      format(c0.name, background_color_value))
c0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of checkbox "c0" again
print('Requesting background color of checkbox "{}" ...'.format(c0.name))
response = c0.Get_background_color_bco()
print('Background color of checkbox "{}" is: "{}"'.format(c0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the font color of checkbox "c0"
print('Requesting font color of checkbox "{}" ...'.format(c0.name))
response = c0.Get_font_color_pco()
print('Font color of checkbox "{}" is: "{}"'.format(c0.name, response))
print()

time.sleep(1)

# enable checkbox "c0" again to make change in font color visible
c0.setValue(1)

# modify the font color of checkbox "c0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of checkbox "{}" to "{}"'.
      format(c0.name, font_color_value))
c0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of checkbox "c0" again
print('Requesting font color of checkbox "{}" ...'.format(c0.name))
response = c0.Get_font_color_pco()
print('Font color of checkbox "{}" is: "{}"'.format(c0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
