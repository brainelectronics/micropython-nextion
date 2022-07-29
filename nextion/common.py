#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Common

Common functions shared accross all Nextion elements

Check the description of Mixin
https://realpython.com/lessons/multiple-inheritance-python/
"""

# system packages
from time import sleep


class CommonError(Exception):
    """Base class for exceptions in this module."""
    pass


class Common(object):
    """docstring for Common"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init gauge

        :param      nh:    The Nextion hardware interface object
        :type       nh:    NexHardware
        :param      pid:   The page ID
        :type       pid:   int
        :param      cid:   The component ID
        :type       cid:   int
        :param      name:  The component name
        :type       name:  str
        """
        self._pid = pid
        self._cid = cid
        self._name = name
        self._nh = nh

    @property
    def pid(self) -> int:
        """
        Get page ID of element

        :returns:   Page ID
        :rtype:     int
        """
        return self._pid

    @property
    def cid(self) -> int:
        """
        Get component ID of element

        :returns:   Component ID
        :rtype:     int
        """
        return self._cid

    @property
    def name(self) -> str:
        """
        Get name of element

        :returns:   Name of element
        :rtype:     str
        """
        return self._name

    def hide(self) -> bool:
        """
        Hide component on screen

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "vis {},0".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def show(self) -> bool:
        """
        Show component on screen

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "vis {},1".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()


class CommonBackgroundColorMixin(object):
    """docstring for CommonBackgroundColorMixin"""
    def Get_background_color_bco(self) -> int:
        """
        Get background color attribute of component

        :returns:   The background color
        :rtype:     int
        """
        cmd = "get {}.bco".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_background_color_bco(self, number: int) -> bool:
        """
        Set background color attribute of component

        :param      number:  The background color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.bco={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()


class CommonFontMixin(object):
    """docstring for CommonFontMixin"""
    def Get_font_color_pco(self) -> int:
        """
        Get font color attribute of component

        :returns:   The font color
        :rtype:     int
        """
        cmd = "get {}.pco".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_font_color_pco(self, number: int) -> bool:
        """
        Set font color attribute of component

        :param      number:  The font color number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.pco={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def getFont(self) -> int:
        """
        Get font attribute of component

        :returns:   The font color
        :rtype:     int
        """
        cmd = "get {}.font".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def setFont(self, number: int) -> bool:
        """
        Set font attribute of component

        :param      number:  The font number
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.font={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()


class CommonPositionMixin(object):
    """docstring for CommonPositionMixin"""
    def Get_place_xcen(self) -> int:
        """
        Get xcen attribute of component

        :returns:   The x position
        :rtype:     int
        """
        cmd = "get {}.xcen".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_place_xcen(self, number: int) -> bool:
        """
        Get xcen attribute of component

        :param      number:  The new x position
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.xcen={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()

    def Get_place_ycen(self) -> int:
        """
        Get ycen attribute of component

        :returns:   The y position
        :rtype:     int
        """
        cmd = "get {}.ycen".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def Set_place_ycen(self, number: int) -> bool:
        """
        Get ycen attribute of component

        :param      number:  The new y position
        :type       number:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.ycen={}".format(self.name, number)
        self._nh.sendCommand(cmd)
        cmd = "ref {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()


class CommonTextMixin(object):
    """docstring for CommonTextMixin"""
    def getText(self) -> str:
        """
        Get text attribute of component

        :returns:   The text.
        :rtype:     str
        """
        cmd = "get {}.txt".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetString()

    def setText(self, text: str) -> bool:
        """
        Set text attribute of component

        :param      text:  The text
        :type       text:  str

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = '{}.txt="{}"'.format(self.name, text)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()


class CommonValueMixin(object):
    """docstring for CommonValueMixin"""
    def getValue(self) -> int:
        """
        Get value attribute of component

        :returns:   The value.
        :rtype:     int
        """
        cmd = "get {}.val".format(self.name)
        self._nh.sendCommand(cmd)
        sleep(0.1)  # necessary, data might not be available otherwise
        return self._nh.recvRetNumber()

    def setValue(self, value: int) -> bool:
        """
        Set value attribute of component

        :param      text:  The value
        :type       text:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "{}.val={}".format(self.name, value)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
