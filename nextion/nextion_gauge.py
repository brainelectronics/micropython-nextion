#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexGauge

Functions to interact with a Nextion Gauge element
"""

# custom packages
from .common import Common, CommonBackgroundColorMixin, CommonFontMixin, CommonValueMixin


class NexGaugeError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexGauge(Common, CommonBackgroundColorMixin, CommonFontMixin, CommonValueMixin):
    """docstring for NexGauge"""
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
        super().__init__(nh, pid, cid, name)

        CommonFontMixin_unsupported_functions = [
            "getFont",
            "setFont",
        ]
        for attr_name in CommonFontMixin_unsupported_functions:
            delattr(CommonFontMixin, attr_name)
