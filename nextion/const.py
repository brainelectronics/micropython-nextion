#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Const

This file contains the constant definitions of all Nextion commands
"""

from micropython import const

# function codes
# defined as const(), see https://github.com/micropython/micropython/issues/573
#: Command finished
NEX_RET_CMD_FINISHED = const(0x01)
#: Event launched
NEX_RET_EVENT_LAUNCHED = const(0x88)
#: Event upgraded
NEX_RET_EVENT_UPGRADED = const(0x89)
#: Event touch head
NEX_RET_EVENT_TOUCH_HEAD = const(0x65)
#: Event position head
NEX_RET_EVENT_POSITION_HEAD = const(0x67)
#: Event sleep position head
NEX_RET_EVENT_SLEEP_POSITION_HEAD = const(0x68)
#: Current page ID head
NEX_RET_CURRENT_PAGE_ID_HEAD = const(0x66)
#: String head
NEX_RET_STRING_HEAD = const(0x70)
#: Number head
NEX_RET_NUMBER_HEAD = const(0x71)
#: Invalid command
NEX_RET_INVALID_CMD = const(0x00)
#: Invalid component ID
NEX_RET_INVALID_COMPONENT_ID = const(0x02)
#: Invalid page ID
NEX_RET_INVALID_PAGE_ID = const(0x03)
#: Invalid picture ID
NEX_RET_INVALID_PICTURE_ID = const(0x04)
#: Invalid font ID
NEX_RET_INVALID_FONT_ID = const(0x05)
#: Invalid baudrate
NEX_RET_INVALID_BAUD = const(0x11)
#: Invalid variable
NEX_RET_INVALID_VARIABLE = const(0x1A)
#: Invalid operation
NEX_RET_INVALID_OPERATION = const(0x1B)

# non standard define, but helpful in any case
#: End command
NEX_END_CMD = b'\xFF\xFF\xFF'
