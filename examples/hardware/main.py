#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with the display brightness, sleep mode and reset
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexCheckbox, NexButton, NexHardware, NexNumber

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# decrease display brightness to 50%
display_brightness = 50
print('Decreasing display brightness to {}%...'.format(display_brightness))
nh.brightness(display_brightness)
print()

time.sleep(1)

# activate sleep mode of display
print('Activating display sleep mode for 5 seconds')
nh.sleep(True)
time.sleep(5)
print('Wakeup display again')
nh.sleep(False)

time.sleep(1)

# manipulate display content to demonstrate display reset afterwards
print('Manipulating display content a little bit ...')
b0 = NexButton(nh, 0, 1, "b0")
b0.setText("something")
n0 = NexNumber(nh, 0, 1, "n0")
n0.setValue(randint(1, 100))
c0 = NexCheckbox(nh, 0, 1, "c0")
c0.setValue(0)
print('Reset display to default in 5 seconds')
time.sleep(5)
nh.reset()
print('Fully brightness restored, all elements show the default value')
print()

time.sleep(1)

# hide button "b0" on screen
print('Hiding button "{}" ...'.format(b0.name))
b0.hide()
print()

time.sleep(5)

# show button "b0" again on screen
print('Showing button "{}" again ...'.format(b0.name))
b0.show()
print()

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
