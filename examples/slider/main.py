#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a slider element
"""

# system packages
from random import choice, randint
import time

# custom packages
from nextion import NexSlider, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a slider instance
h0 = NexSlider(nh, 0, 1, "h0")

# ============================================================================
# ============================== Example values ==============================
# new values of slider
# avoid something close to zero or close to 50
slider_value = choice([randint(5, 40), randint(60, 100)])
background_color_value = 63488  # red
font_color_value = 31           # blue
pointer_thickness = 5
cursor_height = 5
slider_max = 150
slider_min = 10

# ============================================================================
# ============================== Value functions =============================
# request the value of slider "h0"
print('Requesting slider "{}" value ...'.format(h0.name))
response = h0.getValue()
print('Slider "{}" value is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify slider "h0" showing "50" by default
print('Set slider "{}" to "{}"'.format(h0.name, slider_value))
h0.setValue(slider_value)
print()

time.sleep(1)

# request the value of slider "h0" again
print('Requesting slider "{}" value ...'.format(h0.name))
response = h0.getValue()
print('slider "{}" value is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != slider_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of slider "h0"
print('Requesting background color of slider "{}" ...'.format(h0.name))
response = h0.Get_background_color_bco()
print('Background color of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the background color of slider "h0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of slider "{}" to "{}"'.
      format(h0.name, background_color_value))
h0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of slider "h0" again
print('Requesting background color of slider "{}" ...'.format(h0.name))
response = h0.Get_background_color_bco()
print('Background color of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of slider "h0"
print('Requesting font color of slider "{}" ...'.format(h0.name))
response = h0.Get_font_color_pco()
print('Font color of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the font color of slider "h0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of slider "{}" to "{}"'.
      format(h0.name, font_color_value))
h0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of slider "h0" again
print('Requesting font color of slider "{}" ...'.format(h0.name))
response = h0.Get_font_color_pco()
print('Font color of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================ Pointer functions =============================
# request the pointer thickness of slider "h0"
print('Requesting pointer thickness of slider "{}" ...'.format(h0.name))
response = h0.Get_pointer_thickness_wid()
print('Pointer thickness of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the pointer thickness of slider "h0"
print('Set pointer thickness of slider "{}" to "{}"'.
      format(h0.name, pointer_thickness))
h0.Set_pointer_thickness_wid(pointer_thickness)
print()

time.sleep(1)

# request the pointer thickness of slider "h0" again
print('Requesting pointer thickness of slider "{}" ...'.format(h0.name))
response = h0.Get_pointer_thickness_wid()
print('Pointer thickness of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != pointer_thickness:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================ Special functions =============================
# ============================================================================
# ============================= Cursor functions =============================
# request the cursor height of slider "h0"
print('Requesting cursor height of slider "{}" ...'.format(h0.name))
response = h0.Get_cursor_height_hig()
print('Cursor height of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the cursor height of slider "h0"
print('Set cursor height of slider "{}" to "{}"'.
      format(h0.name, cursor_height))
h0.Set_cursor_height_hig(cursor_height)
print()

time.sleep(1)

# request the cursor height of slider "h0" again
print('Requesting cursor height of slider "{}" ...'.format(h0.name))
response = h0.Get_cursor_height_hig()
print('Cursor height of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != cursor_height:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# =========================== Value Limit functions ==========================
# request the maximum value of slider "h0"
print('Requesting maximum value of slider "{}" ...'.format(h0.name))
response = h0.getMaxval()
print('Maximum value of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the maximum value of slider "h0"
print('Set maximum value of slider "{}" to "{}"'.
      format(h0.name, slider_max))
h0.setMaxval(slider_max)
print()

time.sleep(1)

# request the maximum value of slider "h0" again
print('Requesting maximum value of slider "{}" ...'.format(h0.name))
response = h0.getMaxval()
print('cursor height of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != slider_max:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# request the minimum value of slider "h0"
print('Requesting minimum value of slider "{}" ...'.format(h0.name))
response = h0.getMinval()
print('Minimum value of slider "{}" is: "{}"'.format(h0.name, response))
print()

time.sleep(1)

# modify the minimum value of slider "h0"
print('Set minimum value of slider "{}" to "{}"'.
      format(h0.name, slider_min))
h0.setMinval(slider_min)
print()

time.sleep(1)

# request the minimum value of slider "h0" again
print('Requesting minimum value of slider "{}" ...'.format(h0.name))
response = h0.getMinval()
print('cursor height of slider "{}" is: "{}"'.format(h0.name, response))
print()

# sanity check
if response != slider_min:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
