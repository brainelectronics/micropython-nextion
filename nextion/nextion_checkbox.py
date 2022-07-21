#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexCheckbox

Functions to interact with a Nextion Checkbox element
"""

# custom packages
from .common import Common, CommonValueMixin


class NexCheckboxError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexCheckbox(Common, CommonValueMixin):
    """docstring for NexCheckbox"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init checkbox

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
