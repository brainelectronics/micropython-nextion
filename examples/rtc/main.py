#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with a RTC
"""

# system packages
import time

# custom packages
from nextion import NexHardware, NexRtc

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a RTC instance
rtc = NexRtc(nh)

# ============================================================================
# ============================ Sync time with NTP ============================
try:
    import network
    import ntptime

    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        ntptime.settime()
    else:
        print('Device not connected to the internet, using available time')
except Exception as e:
    print('Unexpected exception {} occured, using available time'.format(e))

# cut off weekday and yearday, keep [year, month, mday, hour, minute, second]
localtime = list(time.localtime())[0:6]

# ============================================================================
# ============================ Set RTC functions =============================
# set RTC time to list of integers '[2022, 7, 30, 18, 21, 45]'
print('Set RTC time to: {}'.format(localtime))
rtc.write_rtc_time(localtime)
print()

time.sleep(1)

# set RTC time to time string '2022,07,30,18,21,45'
localtime_str = ','.join('{:02d}'.format(x) for x in localtime)
print('Set RTC time to: "{}"'.format(localtime_str))
rtc.write_rtc_time(localtime_str)
print()

time.sleep(1)

# set only year of RTC
print('Set only year of RTC to: "{}"'.format(localtime[0]))
rtc.write_rtc_time('year', localtime[0])
print()

time.sleep(1)

# ============================================================================
# ============================ Get RTC functions =============================
# get RTC time as string
response = rtc.read_rtc_time('str')
print('Timestamp from RTC as string: "{}"'.format(response))
print()

time.sleep(1)

# get RTC time as list of integers
response = rtc.read_rtc_time('int')
print('Timestamp from RTC list of integers: "{}"'.format(response))
print()

time.sleep(1)

# get available time types from RTC one by one
print('Get individual time types from RTC...')
for time_type in rtc.time_types:
    response = rtc.read_rtc_time(time_type)
    print('{} by RTC: "{}"'.format(time_type, response))
print()

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
