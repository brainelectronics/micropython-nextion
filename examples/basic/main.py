#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to manipulate all elements of page 0 with basic command calls
"""

# system packages
import time

# custom packages
from nextion import NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# ============================================================================
# ============================== Text examples ===============================
# modify text field "t0" showing "newtxt" by default
print('Set text field "t0" to "asdf"')
cmd = 't0.txt="asdf"'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================= Number examples ==============================
# modify number field "n0" showing "0" by default
print('Set number field "n0" to "93"')
cmd = 'n0.val=93'
nh.sendCommand(cmd)
print()

time.sleep(1)

# modify float field "x0" showing "0.0" by default
print('Set float field "x0" to "20.1"')
cmd = 'x0.val=201'  # last digit is value after "."
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================= Button examples ==============================
# modify button "b0" showing "newtxt" by default
print('Set button "b0" to "btn txt"')
cmd = 'b0.txt="btn txt"'
nh.sendCommand(cmd)
print()

time.sleep(1)

# modify dual state button "bt0" showing "newtxt" by default
print('Set dual state button "bt0" to "dsb txt"')
cmd = 'bt0.txt="dsb txt"'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# =========================== Progressbar examples ===========================
# modify progressbar "j0" showing "50%" by default
print('Set progressbar "j0" to "20"')
cmd = 'j0.val=20'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================= Slider examples ==============================
# modify slider "h0" showed in center position by default
print('Set slider "h0" to "80"')
cmd = 'h0.val=80'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================ Checkbox examples =============================
# modify checkbox "c0" being checked by default
print('Set checkbox "c0" to "unchecked"')
cmd = 'c0.val=0'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================== Radio examples ==============================
# modify radio button "r0" being enabled by default
print('Set radio butto "r0" to "disabled"')
cmd = 'r0.val=0'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================== Gauge examples ==============================
# modify gauge "z0" pointing to the left by default
print('Set gauge "z0" to "135" (degree)')
cmd = 'z0.val=135'
nh.sendCommand(cmd)
print()

time.sleep(1)

# ============================================================================
# ============================ Waveform examples =============================
# add several datapoints to waveform "s0"
print('Add several datapoints to waveform "s0"')
for x in range(0, 50):
    cmd = 'add 14,0,{}'.format(x)
    nh.sendCommand(cmd)
    time.sleep(0.1)

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
