#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a dual state button element
"""

# system packages
import time

# custom packages
from nextion import NexDSButton, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a dual state button instance
bt0 = NexDSButton(nh, 0, 1, "bt0")

# ============================================================================
# ============================== Example values ==============================
# new values for dual state button
button_text = "btn txt"
button_value = 1    # 1 is active (green), 0 is inactive (grey)
background_color_value = 63488  # red
font_color_value = 31   # blue
pressed_background_color_value = 64480  # orange
x_offset = 20
y_offset = 20

# ============================================================================
# =========================== Text+Value functions ===========================
# request the text of dual state button "bt0"
print('Requesting dual state button "{}" text ...'.format(bt0.name))
response_text = bt0.getText()
print('Dual state button "{}" text is: "{}"'.format(bt0.name, response_text))
print()

# request the value of dual state button "bt0"
print('Requesting dual state button "{}" value ...'.format(bt0.name))
response_value = bt0.getValue()
print('Dual state button "{}" value is: "{}"'.format(bt0.name, response_value))
print()

time.sleep(1)

# modify dual state button "bt0" showing "newtxt" by default
print('Set dual state button "{}" text to "{}"'.format(bt0.name, button_text))
bt0.setText(button_text)
print()

# modify dual state button "bt0" being released by default
print('Set dual state button "{}" state to "{}"'.
      format(bt0.name, button_value))
bt0.setValue(button_value)
print()

time.sleep(1)

# request the text of dual state button "bt0" again
print('Requesting dual state button "{}" text ...'.format(bt0.name))
response_text = bt0.getText()
print('Dual state button "{}" text is: "{}"'.format(bt0.name, response_text))
print()

# request the value of dual state button "bt0" again
print('Requesting dual state button "{}" value ...'.format(bt0.name))
response_value = bt0.getValue()
print('Dual state button "{}" value is: "{}"'.format(bt0.name, response_value))
print()

# sanity check
if response_text != button_text:
    print('WARNING: GET text value did not match SET text value')
if response_value != button_value:
    print('WARNING: GET state value did not match SET state value')

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of dual state button "bt0"
print('Requesting background color of dual state button "{}" ...'.
      format(bt0.name))
response = bt0.Get_state0_color_bco0()
print('Background color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

time.sleep(1)

# modify the background color of dual state button "bt0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of dual state button "{}" to "{}"'.
      format(bt0.name, background_color_value))
bt0.Set_state0_color_bco0(background_color_value)
print()

time.sleep(1)

# request the background color of dual state button "bt0" again
print('Requesting background color of dual state button "{}" ...'.
      format(bt0.name))
response = bt0.Get_state0_color_bco0()
print('Background color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of dual state button "bt0"
print('Requesting font color of dual state button "{}" ...'.format(bt0.name))
response = bt0.Get_font_color_pco()
print('Font color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

time.sleep(1)

# modify the font color of dual state button "bt0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of dual state button "{}" to "{}"'.
      format(bt0.name, font_color_value))
bt0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of dual state button "bt0" again
print('Requesting font color of dual state button "{}" ...'.format(bt0.name))
response = bt0.Get_font_color_pco()
print('Font color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================ Position functions ============================
# request the x/y position of dual state button "bt0" again
print('Requesting x/y position of dual state button "{}" ...'.format(bt0.name))
x_position = bt0.Get_place_xcen()
y_position = bt0.Get_place_ycen()
print('Position of dual state button "{}" is: "x={}", "y={}"'.
      format(bt0.name, x_position, y_position))
print()

x_position += x_offset
y_position += y_offset

# modify the x/y position of dual state button "bt0"
print('Set x/y position of dual state button "{}" to "x={}", "y={}"'.
      format(bt0.name, x_position, y_position))
bt0.Set_place_xcen(x_position)
bt0.Set_place_ycen(y_position)
print()

time.sleep(1)

# ============================================================================
# ============================ Special functions =============================
# request the pressed background color of dual state button "bt0"
print('Requesting pressed background color of dual state button "{}" ...'.
      format(bt0.name))
response = bt0.Get_state1_color_bco1()
print('Pressed background color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

time.sleep(1)

# modify the pressed background color of dual state button "bt0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set pressed background color of dual state button "{}" to "{}"'.
      format(bt0.name, pressed_background_color_value))
bt0.Set_state1_color_bco1(pressed_background_color_value)
print()

time.sleep(1)

# request the pressed background color of dual state button "bt0" again
print('Requesting pressed background color of dual state button "{}" ...'.
      format(bt0.name))
response = bt0.Get_state0_color_bco0()
print('Pressed background color of dual state button "{}" is: "{}"'.
      format(bt0.name, response))
print()

# sanity check
if response != pressed_background_color_value:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
