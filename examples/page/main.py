#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a page element
"""

# system packages
import time

# custom packages
from nextion import NexPage, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create page instances
page0 = NexPage(nh, 0, 0, "page0")
page1 = NexPage(nh, 1, 0, "page1")
page2 = NexPage(nh, 2, 0, "page2")

# show the default page 0
print('Showing page "{}" ...'.format(page0.name))
page0.show()
print()

time.sleep(1)

# show the page 1
print('Showing page "{}" ...'.format(page1.name))
page1.show()
print()

time.sleep(1)

# show the page 2
print('Showing page "{}" ...'.format(page2.name))
page2.show()
print()

time.sleep(1)

# show the page 0 again
print('Showing page "{}" ...'.format(page0.name))
page0.show()
print()

print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
