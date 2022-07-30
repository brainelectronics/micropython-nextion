#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexNumber

Functions to interact with a Nextion Number element
"""

# system packages
from time import sleep

# custom packages
from .common import Common, CommonBackgroundColorMixin, CommonFontMixin, \
    CommonPositionMixin, CommonValueMixin


class NexNumberError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexNumber(Common, CommonBackgroundColorMixin, CommonFontMixin,
                CommonPositionMixin, CommonValueMixin):
    """docstring for NexNumber"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init number

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

    def Get_number_length(self) -> int:
        """
        Get length attribute of component

        :returns:   The number length
        :rtype:     int
        """
        cmd = "get {}.lenth".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_number_length(self, number: int) -> bool:
        """
        Set length attribute of component

        :param      number:  The number length
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.lenth={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
