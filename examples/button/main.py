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

# new text of button
button_text = "btn txt"

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

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
