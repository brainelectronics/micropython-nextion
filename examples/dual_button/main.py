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

# new text and value for dual state button
button_text = "btn txt"
button_value = 1    # 1 is active (green), 0 is inactive (grey)

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
print('Set dual state button "{}" state to "{}"'.format(bt0.name, button_value))
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

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
