#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a button element
"""

# system packages
import time

# custom packages
from nextion import NexButton, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a button instance
b0 = NexButton(nh, 0, 1, "b0")

# ============================================================================
# ============================== Example values ==============================
# new values of button
button_text = "btn txt"
background_color_value = 63488  # red
font_color_value = 31           # blue
pressed_background_color_value = 64480  # orange
pressed_font_color_value = 2047         # cyan
x_offset = 20
y_offset = 20

# ============================================================================
# ============================== Text functions ==============================
# request the text of button "b0"
print('Requesting button "{}" text ...'.format(b0.name))
response = b0.getText()
print('Button "{}" text is: "{}"'.format(b0.name, response))
print()

time.sleep(1)

# modify button "b0" showing "newtxt" by default
print('Set button "{}" to "{}"'.format(b0.name, button_text))
b0.setText(button_text)
print()

time.sleep(1)

# request the text of button "b0" again
print('Requesting button "{}" text ...'.format(b0.name))
response = b0.getText()
print('Button "{}" text is: "{}"'.format(b0.name, response))
print()

# sanity check
if response != button_text:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of button "b0"
print('Requesting background color of button "{}" ...'.format(b0.name))
response = b0.Get_background_color_bco()
print('Background color of button "{}" is: "{}"'.format(b0.name, response))
print()

time.sleep(1)

# modify the background color of button "b0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of button "{}" to "{}"'.
      format(b0.name, background_color_value))
b0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of button "b0" again
print('Requesting background color of button "{}" ...'.format(b0.name))
response = b0.Get_background_color_bco()
print('Background color of button "{}" is: "{}"'.format(b0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of button "b0"
print('Requesting font color of button "{}" ...'.format(b0.name))
response = b0.Get_font_color_pco()
print('Font color of button "{}" is: "{}"'.format(b0.name, response))
print()

time.sleep(1)

# modify the font color of button "b0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of button "{}" to "{}"'.
      format(b0.name, font_color_value))
b0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of button "b0" again
print('Requesting font color of button "{}" ...'.format(b0.name))
response = b0.Get_font_color_pco()
print('Font color of button "{}" is: "{}"'.format(b0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================ Position functions ============================
# request the x/y position of button "b0" again
print('Requesting x/y position of button "{}" ...'.format(b0.name))
x_position = b0.Get_place_xcen()
y_position = b0.Get_place_ycen()
print('Position of button "{}" is: "x={}", "y={}"'.
      format(b0.name, x_position, y_position))
print()

x_position += x_offset
y_position += y_offset

# modify the x/y position of button "b0"
print('Set x/y position of button "{}" to "x={}", "y={}"'.
      format(b0.name, x_position, y_position))
b0.Set_place_xcen(x_position)
b0.Set_place_ycen(y_position)
print()

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
