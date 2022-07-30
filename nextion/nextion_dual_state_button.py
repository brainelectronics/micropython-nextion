#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexDSButton

Functions to interact with a Nextion dual state Button element
"""

# system packages
from time import sleep

# custom packages
from .common import Common, CommonFontMixin, CommonPositionMixin, \
    CommonTextMixin, CommonValueMixin


class NexDSButtonError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexDSButton(Common, CommonFontMixin, CommonPositionMixin,
                  CommonTextMixin, CommonValueMixin):
    """docstring for NexDSButton"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init dual state button

        :param      nh:    The Nextion hardware interface object
        :type       nh:    NexHardware
        :param      pid:   The page ID
        :type       pid:   int
        :param      cid:   The component ID
        :type       cid:   int
        :param      name:  The component name
        :type       name:  str
        """
        super().__init__(nh, pid, cid, name)

    def Get_state0_color_bco0(self) -> int:
        """
        Get bco0 attribute of component

        :returns:   The background color
        :rtype:     int
        """
        cmd = "get {}.bco0".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_state0_color_bco0(self, number: int) -> bool:
        """
        Set bco0 attribute of component

        :param      number:  The background color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.bco0={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_state1_color_bco1(self) -> int:
        """
        Get bco1 attribute of component

        :returns:   The background color
        :rtype:     int
        """
        cmd = "get {}.bco1".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_state1_color_bco1(self, number: int) -> bool:
        """
        Set bco1 attribute of component

        :param      number:  The background color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.bco1={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
