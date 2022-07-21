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

# new text of button
textfield_text = "other txt"

# request the text textfield "t0"
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

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
