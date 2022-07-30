#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to perform an update of the Nextion display content
"""

# system packages
import time

# custom packages
from nextion import NexHardware, NexUpload

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a upload instance
nex_download = NexUpload(nh, "everything.tft", 115200)

# ============================================================================
# ============================ Special functions =============================
# print file infos
print('Update file name: "{}" with size of "{}" byte'.
      format(nex_download.file_name, nex_download.file_size))

# perform update
print('Performing update, please wait ...')
result = nex_download.upload()
if result:
    print('Update done successfully')
else:
    print('Update failed')
print()

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
