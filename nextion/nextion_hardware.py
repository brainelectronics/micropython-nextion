#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Common

This class performs the basic and common interactions with the Nextion display

Known issues
    - sendCommand uses the default timeout, but should use timeout = 0
      https://github.com/micropython/micropython/issues/3434
"""

# system packages
from machine import UART
from time import ticks_diff, ticks_ms
import ulogging as logging

# custom packages
from .typing import Optional
from . import const as Const


class NexHardwareError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexHardware(object):
    """docstring for NexHardware"""
    def __init__(self, rx_pin: int, tx_pin: int, baudrate: Optional[int] = 9600, timeout: Optional[int] = 100, invert: Optional[int] = 0, logger: Optional[logging.Logger] = None) -> None:
        """
        Init hardware interface

        :param      rx_pin:    The UART RX
        :type       rx_pin:    int
        :param      tx_pin:    The UART TX
        :type       tx_pin:    int
        :param      baudrate:  The communication baudrate
        :type       baudrate:  int
        :param      timeout:   The communication timeout
        :type       timeout:   int
        :param      invert:    Specify inverted communication lines
        :type       invert:    see MicroPython UART docs
        :param      logger:    The logger
        :type       logger:    logging.Logger
        """
        if logger is None:
            logger = NexHardware.create_logger(logger_name=self.__class__.__name__)
            logger.setLevel(level=logging.WARNING)
        self._logger = logger
        self._logger.disabled = False

        self._tx_pin = tx_pin
        self._rx_pin = rx_pin
        self._baudrate = baudrate
        self._timeout = timeout
        self._invert = invert

        self._uart = UART(
            1,
            tx=self._tx_pin,
            rx=self._rx_pin,
            baudrate=self._baudrate,
            timeout=self._timeout,
            invert=self._invert)

        self._initialized = False

    @staticmethod
    def create_logger(logger_name: Optional[str] = None) -> logging.Logger:
        """
        Create a logger.

        :param      logger_name:  The logger name
        :type       logger_name:  str, optional

        :returns:   Configured logger
        :rtype:     logging.Logger
        """
        logging.basicConfig(level=logging.INFO)

        if logger_name and (isinstance(logger_name, str)):
            logger = logging.getLogger(logger_name)
        else:
            logger = logging.getLogger(__name__)

        # set the logger level to DEBUG if specified differently
        logger.setLevel(logging.DEBUG)

        return logger

    def _uart_init(self) -> None:
        """Init UART instance"""
        if self._uart:
            self._uart.init(
                tx=self._tx_pin,
                rx=self._rx_pin,
                baudrate=self._baudrate,
                timeout=self._timeout,
                invert=self._invert)

    def nexInit(self) -> bool:
        """
        Init Nextion interface to display

        :returns:   Result of init, True on success, False otherwise
        :rtype:     bool
        """
        ret1 = False
        ret2 = False

        self._uart_init()

        self.sendCommand("")
        self.sendCommand("bkcmd=1")
        ret1 = self.recvRetCommandFinished()
        self.sendCommand("page 0")
        ret2 = self.recvRetCommandFinished()

        self._initialized = True

        return ret1 & ret2

    def sleep(self, state: bool) -> None:
        """
        Control display sleep state

        :param      state:  Flag, True is sleep mode, False is wakeup
        :type       state:  bool
        """
        cmd = "sleep={}".format(int(state))
        self.sendCommand(cmd)

    def brightness(self, value: int) -> None:
        """
        Set brightness of display

        :param      value:  The value in percent [0, 100]
        :type       value:  int
        """
        cmd = "dim={}".format(int(value))
        self.sendCommand(cmd)

    def reset(self) -> None:
        """Reset display like on a power cycle"""
        cmd = "rest"
        self.sendCommand(cmd)

    def nexLoop(self):
        pass

    def recvRetNumber(self, timeout: int = 100) -> int:
        """
        Receive a uint32_t number

        :param      timeout:  The communication timeout
        :type       timeout:  int

        :returns:   Received number
        :rtype:     int
        """
        if timeout != self._timeout:
            _old_timeout = self._timeout
            self._timeout = timeout
            self._uart_init()
            self._timeout = _old_timeout

        # ret = False
        temp = bytearray(8)
        number = 0

        # C implementation requires a pointer to a number as argument
        # Python can directly return the string :)
        # if not number:
        #     self._logger.debug("recvRetNumber err")
        #     return ret

        # function not available in MicroPython, see
        # https://github.com/micropython/micropython/issues/3434
        # self._uart.timeout = timeout

        if self._uart.any() != len(temp):
            self._logger.debug("recvRetNumber err")
            # return ret
            return number

        # at least len(buf) bytes are read if not stopped earlier by a timeout
        self._uart.readinto(temp)
        self._logger.debug(''.join('0x{:02x} '.format(i) for i in temp))

        if ((temp[0] == Const.NEX_RET_NUMBER_HEAD) and
                (temp[5] == 0xFF) and (temp[6] == 0xFF) and (temp[7] == 0xFF)):
            number = (temp[4] << 24) | (temp[3] << 16) | (temp[2] << 8) | (temp[1])
            # ret = True

        # if ret:
        #     self._logger.debug("recvRetNumber: {}".format(number))
        self._logger.debug("recvRetNumber: {}".format(number))

        # return ret
        return number

    def recvRetString(self, timeout: int = 100) -> str:
        """
        Receive a string

        :param      timeout:  The communication timeout
        :type       timeout:  int

        :returns:   Received string
        :rtype:     int
        """
        if timeout != self._timeout:
            _old_timeout = self._timeout
            self._timeout = timeout
            self._uart_init()
            self._timeout = _old_timeout

        # ret = 0
        str_start_flag = False
        cnt_0xff = 0
        temp = ""
        c = 0

        # C implementation requires a pointer to a buffer as argument
        # Python can directly return the string :)
        # if ((buf is None) or (length == 0)):
        #     self._logger.debug("recvRetString[{}, {}]".format(
        #         len(temp), temp))
        #     return ret

        start_ms = ticks_ms()

        # stay inside this while loop at least for the timeout time
        while (ticks_diff(ticks_ms(), start_ms) <= timeout):
            # check amount of available characters
            while self._uart.any():
                # can not decode received data here, as it might not be UTF-8
                # use "self._uart.readinto(buf, 1)" to avoid the call of
                # ".to_bytes(1, 'little')" later
                c = self._uart.read(1)

                if str_start_flag:
                    if c == (0xFF).to_bytes(1, 'little'):
                        cnt_0xff += 1
                        if cnt_0xff >= 3:
                            # 3x 0xFF marks the end of the message, exit
                            break
                    else:
                        temp += c.decode('utf-8')
                elif c == (Const.NEX_RET_STRING_HEAD).to_bytes(1, 'little'):
                    str_start_flag = True

            if cnt_0xff >= 3:
                break

        # ret = len(temp)
        #
        # ret = ret > len ? len : ret;
        # not required at all, this is Python, not C
        # if ret > length:
        #     ret = length
        # else:
        #     ret = ret
        #
        # buf = temp

        self._logger.debug("recvRetString[{}, {}]".format(len(temp), temp))

        # return ret
        return temp

    def sendCommand(self, cmd: str) -> None:
        """
        Send a command to the Nextion serial display.

        :param      cmd:  The command
        :type       cmd:  str
        """
        while self._uart.any():
            self._uart.read()

        # function not available in MicroPython, see
        # https://github.com/micropython/micropython/issues/3434
        # self._uart.timeout = 0

        self._uart.write(cmd)
        self._uart.write(Const.NEX_END_CMD)

    def recvRetCommandFinished(self, timeout: int = 100) -> bool:
        """
        Command is executed successfully

        :param      timeout:  The communication timeout
        :type       timeout:  int

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        if timeout != self._timeout:
            _old_timeout = self._timeout
            self._timeout = timeout
            self._uart_init()
            self._timeout = _old_timeout

        ret = False
        temp = bytearray(4)

        # function not available in MicroPython, see
        # https://github.com/micropython/micropython/issues/3434
        # self._uart.timeout = timeout

        # this check has no effect, as ret is False by default
        if self._uart.any() != len(temp):
            self._logger.debug("recvRetCommandFinished err")
            ret = False

        # at least len(buf) bytes are read if not stopped earlier by a timeout
        self._uart.readinto(temp)
        self._logger.debug(''.join('0x{:02x} '.format(i) for i in temp))

        if ((temp[0] == Const.NEX_RET_CMD_FINISHED) and
                (temp[1] == 0xFF) and (temp[2] == 0xFF) and (temp[3] == 0xFF)):
            self._logger.debug("recvRetCommandFinished ok")
            ret = True

        return ret
