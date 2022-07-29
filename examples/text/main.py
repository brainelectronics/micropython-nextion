#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a text element
"""

# system packages
import time

# custom packages
from nextion import NexText, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a textfield instance
t0 = NexText(nh, 0, 1, "t0")

# new values of text
textfield_text = "other txt"
background_color_value = 63488  # red
font_color_value = 31           # blue
x_offset = 20
y_offset = 20

# request the text of textfield "t0"
print('Requesting textfield "{}" text ...'.format(t0.name))
response = t0.getText()
print('Textfield "{}" text is: "{}"'.format(t0.name, response))
print()

time.sleep(1)

# modify textfield "t0" showing "newtxt" by default
print('Set textfield "{}" to "{}"'.format(t0.name, textfield_text))
t0.setText(textfield_text)
print()

time.sleep(1)

# request the text of textfield "t0" again
print('Requesting textfield "{}" text ...'.format(t0.name))
response = t0.getText()
print('Textfield "{}" text is: "{}"'.format(t0.name, response))
print()

# sanity check
if response != textfield_text:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the background color of textfield "t0"
print('Requesting background color of textfield "{}" ...'.format(t0.name))
response = t0.Get_background_color_bco()
print('Background color of textfield "{}" is: "{}"'.format(t0.name, response))
print()

time.sleep(1)

# modify the background color of textfield "t0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of textfield "{}" to "{}"'.
      format(t0.name, background_color_value))
t0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of textfield "t0" again
print('Requesting background color of textfield "{}" ...'.format(t0.name))
response = t0.Get_background_color_bco()
print('Background color of textfield "{}" is: "{}"'.format(t0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the font color of textfield "t0"
print('Requesting font color of textfield "{}" ...'.format(t0.name))
response = t0.Get_font_color_pco()
print('Font color of textfield "{}" is: "{}"'.format(t0.name, response))
print()

time.sleep(1)

# modify the font color of textfield "t0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of textfield "{}" to "{}"'.
      format(t0.name, font_color_value))
t0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of textfield "t0" again
print('Requesting font color of textfield "{}" ...'.format(t0.name))
response = t0.Get_font_color_pco()
print('Font color of textfield "{}" is: "{}"'.format(t0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the x/y position of textfield "t0" again
print('Requesting x/y position of textfield "{}" ...'.format(t0.name))
x_position = t0.Get_place_xcen()
y_position = t0.Get_place_ycen()
print('Position of textfield "{}" is: "x={}", "y={}"'.
      format(t0.name, x_position, y_position))
print()

x_position += x_offset
y_position += y_offset

# modify the x/y position of textfield "t0"
print('Set x/y position of textfield "{}" to "x={}", "y={}"'.
      format(t0.name, x_position, y_position))
t0.Set_place_xcen(x_position)
t0.Set_place_ycen(y_position)
print()

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
