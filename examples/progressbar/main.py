#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a progressbar element
"""

# system packages
from random import choice, randint
import time

# custom packages
from nextion import NexHardware, NexProgressBar

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a progressbar instance
j0 = NexProgressBar(nh, 0, 1, "j0")

# ============================================================================
# ============================== Example values ==============================
# new values of progressbar
# avoid something close to zero or close to 50
progressbar_value = choice([randint(5, 40), randint(60, 100)])
background_color_value = 63488  # red
font_color_value = 31           # blue

# ============================================================================
# ============================== Value functions =============================
# request the value of progressbar "j0" being 50 by default
print('Requesting progressbar "{}" value ...'.format(j0.name))
response = j0.getValue()
print('Progressbar "{}" value is: "{}"'.format(j0.name, response))
print()

time.sleep(1)

# modify progressbar "j0" being checked by default
print('Set progressbar "{}" to "{}"'.format(j0.name, progressbar_value))
j0.setValue(progressbar_value)
print()

time.sleep(1)

# request the value of progressbar "j0" again
print('Requesting progressbar "{}" value ...'.format(j0.name))
response = j0.getValue()
print('Progressbar "{}" value is: "{}"'.format(j0.name, response))
print()

# sanity check
if response != progressbar_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# =========================== Background functions ===========================
# request the background color of progressbar "j0"
print('Requesting background color of progressbar "{}" ...'.format(j0.name))
response = j0.Get_background_color_bco()
print('Background color of progressbar "{}" is: "{}"'.
      format(j0.name, response))
print()

time.sleep(1)

# modify the background color of progressbar "j0" to "red"
# search for RGB565 Colors. Red is "63488" at 65k colors
print('Set background color of progressbar "{}" to "{}"'.
      format(j0.name, background_color_value))
j0.Set_background_color_bco(background_color_value)
print()

time.sleep(1)

# request the background color of progressbar "j0" again
print('Requesting background color of progressbar "{}" ...'.format(j0.name))
response = j0.Get_background_color_bco()
print('Background color of progressbar "{}" is: "{}"'.
      format(j0.name, response))
print()

# sanity check
if response != background_color_value:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# ============================================================================
# ============================== Font functions ==============================
# request the font color of progressbar "j0"
print('Requesting font color of progressbar "{}" ...'.format(j0.name))
response = j0.Get_font_color_pco()
print('Font color of progressbar "{}" is: "{}"'.format(j0.name, response))
print()

time.sleep(1)

# modify the font color of progressbar "j0" to "blue"
# search for RGB565 Colors. Blue is "31" at 65k colors
print('Set font color of progressbar "{}" to "{}"'.
      format(j0.name, font_color_value))
j0.Set_font_color_pco(font_color_value)
print()

time.sleep(1)

# request the font color of progressbar "j0" again
print('Requesting font color of progressbar "{}" ...'.format(j0.name))
response = j0.Get_font_color_pco()
print('Font color of progressbar "{}" is: "{}"'.format(j0.name, response))
print()

# sanity check
if response != font_color_value:
    print('WARNING: GET value did not match SET value')

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
