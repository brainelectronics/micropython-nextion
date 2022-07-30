#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexSlider

Functions to interact with a Nextion Slider element
"""

# system packages
from time import sleep

# custom packages
from .common import Common, CommonBackgroundColorMixin, CommonFontMixin, \
    CommonPointerMixin, CommonValueMixin


class NexSliderError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexSlider(Common, CommonBackgroundColorMixin, CommonFontMixin,
                CommonPointerMixin, CommonValueMixin):
    """docstring for NexSlider"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init slider

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

    def Get_cursor_height_hig(self) -> int:
        """
        Get cursor hig attribute of component

        :returns:   The cursor height.
        :rtype:     number
        """
        cmd = "get {}.hig".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_cursor_height_hig(self, number: int) -> bool:
        """
        Set cursor hig attribute of component

        :param      number:  The number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.hig={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def getMaxval(self) -> int:
        """
        Get the maxval attribute of the component

        :returns:   The maxval
        :rtype:     int
        """
        cmd = "get {}.maxval".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def setMaxval(self, number: int) -> bool:
        """
        Set the maxval attribute of the component

        :param      number:  The new maxval
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.maxval={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def getMinval(self) -> int:
        """
        Get the minval attribute of the component

        :returns:   The minval
        :rtype:     int
        """
        cmd = "get {}.minval".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def setMinval(self, number: int) -> bool:
        """
        Set the minval attribute of the component

        :param      number:  The new minval
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.minval={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
