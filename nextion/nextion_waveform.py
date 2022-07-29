#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexWaveform

Functions to interact with a Nextion Waveform element
"""

# system packages
from time import sleep

# custom packages
from .common import Common, CommonBackgroundColorMixin


class NexWaveformError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexWaveform(Common, CommonBackgroundColorMixin):
    """docstring for NexWaveform"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init waveform

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

    def addValue(self, ch: int, number: int) -> bool:
        """
        Add value to waveform

        :param      ch:      Channel of waveform (0-3)
        :type       ch:      int
        :param      number:  The value to add
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        if ch > 3:
            self._logger.debug("Only channels (0-3) supported by waveform")
            return False

        cmd = "add {},{},{}".format(self.cid, ch, number)
        self._nh.sendCommand(cmd)
        return True

    def clearChannel(self, ch: int) -> bool:
        """
        Clear a channel of the waveform

        :param      ch:   The channel to clear or 255 for all channels
        :type       ch:   int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        if (ch > 3) and (ch != 255):
            self._logger.debug("Only channel (0-3) or all (255) can be cleared")
            return False

        cmd = "cle {},{}".format(self.cid, ch)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
