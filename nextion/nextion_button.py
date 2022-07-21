#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexButton

Functions to interact with a Nextion Button element
"""

# custom packages
from .common import Common, CommonTextMixin, CommonValueMixin


class NexButtonError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexButton(Common, CommonTextMixin, CommonValueMixin):
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
