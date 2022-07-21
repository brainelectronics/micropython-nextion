#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexPage

Functions to interact with a Nextion Page element
"""

# custom packages
from .common import Common


class NexPageError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexPage(Common):
    """docstring for NexPage"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init page

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

    def show(self) -> bool:
        """
        Show itself

        :returns:   True on success, false otherwise
        :rtype:     bool
        """
        cmd = "page {}".format(self.name)
        self._nh.sendCommand(cmd)
        return self._nh.recvRetCommandFinished()
