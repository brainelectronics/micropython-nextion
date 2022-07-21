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
        Set value attribute of component.

        :param      text:  The value
        :type       text:  int

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = '{}.val={}'.format(self.name, value)
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
        Set text attribute of component.

        :param      text:  The text
        :type       text:  str

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = '{}.txt="{}"'.format(self.name, text)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
