#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexDSButton

Functions to interact with a Nextion dual state Button element
"""

# custom packages
from .common import Common, CommonTextMixin, CommonValueMixin


class NexDSButtonError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexDSButton(Common, CommonTextMixin, CommonValueMixin):
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
