#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Boot script

Do initial stuff here, similar to the setup() function on Arduino

Connect to network, create an AccessPoint if connection failed otherwise
"""

# system packages
import esp
import gc
import machine
import network
import time

# set clock speed to 240MHz instead of default 160MHz
# import machine
# machine.freq(240000000)

# disable ESP os debug output
esp.osdebug(None)

# set pin D4 as output (blue LED)
led_pin = machine.Pin(4, machine.Pin.OUT)

# turn onboard LED on
led_pin.value(1)

station = network.WLAN(network.STA_IF)
if station.active() and station.isconnected():
    station.disconnect()
    time.sleep(1)
station.active(False)
time.sleep(1)
station.active(True)

station.connect('SSID', 'PASSWORD')
time.sleep(1)

connection_timeout = 10 * 1000    # WiFi connection timeout in milliseconds
start_ms = time.ticks_ms()
while (time.ticks_diff(time.ticks_ms(), start_ms) <= connection_timeout):
    print('Waiting for WiFi connection...')
    if station.isconnected():
        print('Connected to WiFi')
        print(station.ifconfig())
        break
    time.sleep(1)

result = station.isconnected()
# force an accesspoint creation
# result = False

if result is False:
    # disconnect as/from station and disable WiFi for it
    station.disconnect()
    station.active(False)
    time.sleep(1)

    # create a true AccessPoint without any active Station mode
    accesspoint = network.WLAN(network.AP_IF)

    # activate accesspoint if not yet enabled
    if not accesspoint.active():
        accesspoint.active(True)

    accesspoint_name = "MicroPython AP"
    accesspoint.config(essid=accesspoint_name,
                       authmode=network.AUTH_OPEN,
                       password='',
                       channel=11)

    print('Created Accesspoint: {}'.format(accesspoint_name))

# turn onboard LED off
led_pin.value(0)

print('Restart cause: {}'.format(machine.reset_cause()))

# run garbage collector at the end to clean up
gc.collect()

print('System booted successfully!')
