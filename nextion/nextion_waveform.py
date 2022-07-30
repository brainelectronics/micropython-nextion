#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexWaveform

Functions to interact with a Nextion Waveform element
"""

# system packages
from time import sleep

# custom packages
from .common import Common, CommonBackgroundColorMixin, CommonFontMixin


class NexWaveformError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexWaveform(Common, CommonBackgroundColorMixin, CommonFontMixin):
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

    def Get_grid_color_gdc(self) -> int:
        """
        Get grid color attribute of component

        :returns:   The grid color
        :rtype:     int
        """
        cmd = "get {}.gdc".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_grid_color_gdc(self, number: int) -> bool:
        """
        Set grid color attribute of component

        :param      number:  The grid color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.gdc={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_grid_width_gdw(self) -> int:
        """
        Get grid width attribute of component

        :returns:   The grid width
        :rtype:     int
        """
        cmd = "get {}.gdw".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_grid_width_gdw(self, number: int) -> bool:
        """
        Set grid width attribute of component

        :param      number:  The grid width
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.gdw={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_grid_height_gdh(self) -> int:
        """
        Get grid height attribute of component

        :returns:   The grid height
        :rtype:     int
        """
        cmd = "get {}.gdh".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_grid_height_gdh(self, number: int) -> bool:
        """
        Set grid height attribute of component

        :param      number:  The grid height
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.gdh={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_channel_0_color_pco0(self) -> int:
        """
        Get channel0 pco0 attribute of component

        :returns:   The channel0 pco0
        :rtype:     int
        """
        return self.Get_font_color_pco()

    def Set_channel_0_color_pco0(self, number: int) -> int:
        """
        Set channel0 pco0 attribute of component

        :param      number:  The channel0 pco0
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        return self.Set_font_color_pco(number)
