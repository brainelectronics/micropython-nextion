#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Example on how to interact with the Nextion display GPIO pins
"""

# system packages
from random import randint
import time

# custom packages
from nextion import NexGpio, NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# create a button instance
gpio = NexGpio(nh)

# ============================================================================
# ============================== Example values ==============================
# new values of GPIOs
pwm_pin = 7             # only GPIO4 and GPIO7 support PWM
pwm_frequency = 500     # Hz, all PWM pins have same frequency
pwm_value = randint(0, 100)     # 0 is LOW (off), 100 is HIGH (on)

# ============================================================================
# ============================= Pinmode functions ============================
# set all GPIOs as outputs
print('Set all pins as digital output')
for pin in range(0, 8):
    # outputs are HIGH by default
    gpio.pin_mode(pin, NexGpio.OUTPUT)
print()

time.sleep(1)

# ============================================================================
# =========================== Digital IO functions ===========================
# toggle all pins 5 times LOW/HIGH
print('Toggle all pins 5 times LOW/HIGH with 0.5 sec delay between a change')
for _ in range(0, 5):
    for pin in range(0, 8):
        # set pin LOW
        gpio.digital_write(pin, 0)
        time.sleep(0.5)
        # set pin HIGH
        gpio.digital_write(pin, 1)
        time.sleep(0.5)
print()

time.sleep(1)

# set all GPIOs as inputs
print('Set all pins as digital input')
for pin in range(0, 8):
    gpio.pin_mode(pin, NexGpio.INPUT_PULL_UP)
print()

print('Read all pins state')
for pin in range(0, 8):
    state = gpio.digital_read(pin)
    print('Pin "{}" value is: "{}"'.format(pin, state))
print()

time.sleep(1)

# ============================================================================
# =============================== PWM functions ==============================
# only GPIO4 and GPIO7 support PWM
print('Set GPIO7 pin as PWM output (Buzzer of Expansion Board)')
gpio.pin_mode(pwm_pin, NexGpio.PWM)

# request the PWM frequency
print('Requesting PWM frequency ...')
response = gpio.get_pwmfreq()
print('PWM frequency is: "{}"'.format(response))
print()

time.sleep(1)

# modify PWM frequency to 500 Hz
print('Set PWM frequency to "{}"'.format(pwm_frequency))
gpio.set_pwmfreq(pwm_frequency)
print()

time.sleep(1)

# request the PWM frequency again
print('Requesting PWM frequency ...')
response = gpio.get_pwmfreq()
print('PWM frequency is: "{}"'.format(response))
print()

# sanity check
if response != pwm_frequency:
    print('WARNING: GET value did not match SET value')

time.sleep(1)

# modify PWM value (0, 100)[%]
print('Set PWM of "{}" to "{}"'.format(pwm_pin, pwm_value))
gpio.analog_write(pwm_pin, pwm_value)
print()

# ============================================================================
# ============================= End of example ===============================
print('Returning to REPL in 5 seconds')

# wait for 5 more seconds to safely finish the may still running threads
time.sleep(5)
