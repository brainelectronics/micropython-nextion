#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a number element
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexNumber, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a number instance
n0 = NexNumber(nh, 0, 1, "n0")

# new values of number field
number_value = randint(1, 100)
background_color_value = 63488  # red
font_color_value = 31           # blue
x_offset = 20
y_offset = 20

# request the value of number "n0"
print('Requesting number "{}" value ...'.format(n0.name))
response = n0.getValue()
print('Number field "{}" value is: "{}"'.format(n0.name, response))
print()

time.sleep(1)

# modify number field "n0" showing "0" by default
print('Set number field "{}" to "{}"'.format(n0.name, number_value))
n0.setValue(number_value)
print()

time.sleep(1)

# request the value of number "n0" again
print('Requesting number "{}" value ...'.format(n0.name))
response = n0.getValue()
print('Number field "{}" value is: "{}"'.format(n0.name, response))
print()

# sanity check
if response != number_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the background color of number "n0"
print('Requesting background color of number "{}" ...'.format(n0.name))
response = n0.Get_background_color_bco()
print('Background color of number "{}" is: "{}"'.format(n0.name, response))
print()

time.sleep(1)

# modify the background color of number "n0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of number "{}" to "{}"'.
      format(n0.name, background_color_value))
n0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of number "n0" again
print('Requesting background color of number "{}" ...'.format(n0.name))
response = n0.Get_background_color_bco()
print('Background color of number "{}" is: "{}"'.format(n0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the font color of number "n0"
print('Requesting font color of number "{}" ...'.format(n0.name))
response = n0.Get_font_color_pco()
print('Font color of number "{}" is: "{}"'.format(n0.name, response))
print()

time.sleep(1)

# modify the font color of number "n0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of number "{}" to "{}"'.
      format(n0.name, font_color_value))
n0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of number "n0" again
print('Requesting font color of number "{}" ...'.format(n0.name))
response = n0.Get_font_color_pco()
print('Font color of number "{}" is: "{}"'.format(n0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the x/y position of number "n0" again
print('Requesting x/y position of number "{}" ...'.format(n0.name))
x_position = n0.Get_place_xcen()
y_position = n0.Get_place_ycen()
print('Position of number "{}" is: "x={}", "y={}"'.
      format(n0.name, x_position, y_position))
print()

x_position += x_offset
y_position += y_offset

# modify the x/y position of number "n0"
print('Set x/y position of number "{}" to "x={}", "y={}"'.
      format(n0.name, x_position, y_position))
n0.Set_place_xcen(x_position)
n0.Set_place_ycen(y_position)
print()

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
