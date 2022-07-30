#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexButton

Functions to interact with a Nextion Button element
"""

# custom packages
from .common import Common, CommonBackgroundColorMixin, CommonFontMixin, \
    CommonPositionMixin, CommonTextMixin


class NexButtonError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexButton(Common, CommonBackgroundColorMixin, CommonFontMixin,
                CommonPositionMixin, CommonTextMixin):
    """docstring for NexButton"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init button

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

    def Get_press_background_color_bco2(self) -> int:
        """
        Get the pressed background color

        :returns:   The pressed background color bco2
        :rtype:     int
        """
        cmd = "get {}.bco2".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetNumber()

    def Set_press_background_color_bco2(self, number: int) -> bool:
        """
        Set the pressed background color

        :param      number:  The background color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.bco2={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_press_font_color_pco2(self) -> int:
        """
        Get the pressed font color

        :returns:   The pressed font color pco2
        :rtype:     int
        """
        cmd = "get {}.pco2".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetNumber()

    def Set_press_font_color_pco2(self, number: int) -> bool:
        """
        Set the pressed font color

        :param      number:  The font color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.pco2={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
