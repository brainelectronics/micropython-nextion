#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a gauge element
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexGauge, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a gauge instance
z0 = NexGauge(nh, 0, 1, "z0")

# ============================================================================
# ============================== Example values ==============================
# new values of gauge
gauge_value = randint(10, 350)
background_color_value = 63488  # red
font_color_value = 31           # blue
pointer_thickness = 5

# ============================================================================
# ============================== Value functions =============================
# request the value of gauge "z0"
print('Requesting gauge "{}" value ...'.format(z0.name))
response = z0.getValue()
print('Gauge "{}" value is: "{}"'.format(z0.name, response))
print()

time.sleep(1)

# modify gauge "z0" being checked by default
print('Set gauge "{}" to "{}"'.format(z0.name, gauge_value))
z0.setValue(gauge_value)
print()

time.sleep(1)

# request the value of gauge "z0" again
print('Requesting gauge "{}" value ...'.format(z0.name))
response = z0.getValue()
print('Gauge "{}" value is: "{}"'.format(z0.name, response))
print()

# sanity check
if response != gauge_value:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# =========================== Background functions ===========================
# request the background color of gauge "z0"
print('Requesting background color of gauge "{}" ...'.format(z0.name))
response = z0.Get_background_color_bco()
print('Background color of gauge "{}" is: "{}"'.format(z0.name, response))
print()

time.sleep(1)

# modify the background color of gauge "z0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of gauge "{}" to "{}"'.
      format(z0.name, background_color_value))
z0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of gauge "z0" again
print('Requesting background color of gauge "{}" ...'.format(z0.name))
response = z0.Get_background_color_bco()
print('Background color of gauge "{}" is: "{}"'.format(z0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of gauge "z0"
print('Requesting font color of gauge "{}" ...'.format(z0.name))
response = z0.Get_font_color_pco()
print('Font color of gauge "{}" is: "{}"'.format(z0.name, response))
print()

time.sleep(1)

# modify the font color of gauge "z0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of gauge "{}" to "{}"'.format(z0.name, font_color_value))
z0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of gauge "z0" again
print('Requesting font color of gauge "{}" ...'.format(z0.name))
response = z0.Get_font_color_pco()
print('Font color of gauge "{}" is: "{}"'.format(z0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================ Pointer functions =============================
# request the pointer thickness of gauge "z0"
print('Requesting pointer thickness of gauge "{}" ...'.format(z0.name))
response = z0.Get_pointer_thickness_wid()
print('Pointer thickness of gauge "{}" is: "{}"'.format(z0.name, response))
print()

time.sleep(1)

# modify the pointer thickness of gauge "z0"
print('Set pointer thickness of gauge "{}" to "{}"'.
      format(z0.name, pointer_thickness))
z0.Set_pointer_thickness_wid(pointer_thickness)
print()

time.sleep(1)

# request the pointer thickness of gauge "z0" again
print('Requesting pointer thickness of gauge "{}" ...'.format(z0.name))
response = z0.Get_pointer_thickness_wid()
print('Pointer thickness of gauge "{}" is: "{}"'.format(z0.name, response))
print()

# sanity check
if response != pointer_thickness:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
