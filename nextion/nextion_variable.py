#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexVariable

Functions to interact with a Nextion Variable element
"""

# custom packages
from .common import Common, CommonTextMixin, CommonValueMixin


class NexVariableError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexVariable(Common, CommonTextMixin, CommonValueMixin):
    """docstring for NexVariable"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init variable

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
