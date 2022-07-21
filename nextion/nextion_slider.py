#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexSlider

Functions to interact with a Nextion Slider element
"""

# custom packages
from .common import Common, CommonValueMixin


class NexSliderError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexSlider(Common, CommonValueMixin):
    """docstring for NexSlider"""
    def __init__(self, nh, pid: int, cid: int, name: str) -> None:
        """
        Init slider

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
