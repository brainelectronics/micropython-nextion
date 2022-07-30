#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexGpio

Functions to interact with Nextion GPIOs
"""

# system packages
from time import sleep

# custom packages
from .common import Common


class NexGpioError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexGpio(Common):
    """docstring for NexGpio"""
    INPUT_PULL_UP = 0   # set pin as pull up input
    OUTPUT = 2          # set pin as push pull output
    INPUT_BINDING = 1   # bind Nextion element to falling edge of signal
    PWM = 3             # set pin as PWM output (only GPIO4 and GPIO7)

    def __init__(self, nh) -> None:
        """
        Init GPIO

        :param      nh:    The Nextion hardware interface object
        :type       nh:    NexHardware
        """
        super().__init__(nh, pid=-1, cid=-1, name="gpio")

    def pin_mode(self, port: int, mode: int, control_id: int = 0) -> bool:
        """
        Set GPIO mode

        :param      port:        The GPIO port number
        :type       port:        int
        :param      mode:        The GPIO port mode
                                 0 - Pull on the input
                                 1 - the control input binding
                                 2 - Push-pull output
                                 3 - pwm output
                                 4 - open mode leakage
        :type       mode:        int
        :param      control_id:  The bound CID of other nextion element
        :type       control_id:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "cfgpio {},{},{}".format(port, mode, control_id)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def digital_write(self, port: int, value: int) -> bool:
        """
        Write a HIGH or LOW value to a digital pin

        :param      port:   The GPIO port number
        :type       port:   int
        :param      value:  The value (0 or 1)
        :type       value:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "pio{}={}".format(port, value)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def digital_read(self, port: int) -> int:
        """
        Read a HIGH or a LOW value of a digital pin

        :param      port:  The GPIO port number
        :type       port:  int

        :returns:   Value of specified digital pin, either 1 or 0
        :rtype:     int
        """
        cmd = "get pio{}".format(port)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def analog_write(self, port: int, value: int) -> bool:
        """
        Set analog value (PWM wave) to a pin

        :param      port:   The GPIO port number
        :type       port:   int
        :param      value:  The duty cycle value (0-100)
        :type       value:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "pwm{}={}".format(port, value)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def set_pwmfreq(self, value: int) -> bool:
        """
        Set the PWM output frequency for all pins

        :param      value:  The PWM frequency (1-65535)
        :type       value:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "pwmf={}".format(value)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def get_pwmfreq(self) -> int:
        """
        Get the PWM output frequency

        :returns:   The PWM frequency.
        :rtype:     int
        """
        cmd = "get pwmf"
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()
