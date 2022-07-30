#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexRtc

Functions to interact with Nextion RTC
"""

# system packages
from time import sleep

# custom packages
from .common import Common
from .typing import List, Optional, Union


class NexRtcError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexRtc(Common):
    """docstring for NexRtc"""
    def __init__(self, nh) -> None:
        """
        Init RTC

        :param      nh:    The Nextion hardware interface object
        :type       nh:    NexHardware
        """
        super().__init__(nh, pid=-1, cid=-1, name="rtc")

        self._time_types = ["year", "mon", "day", "hour", "min", "sec", "week"]

    @property
    def time_types(self) -> List[str]:
        """
        Get available time types

        :returns:   Requestable time types from RTC
        :rtype:     List[str]
        """
        return self._time_types

    def write_rtc_time(self, *args, **kwargs) -> bool:
        """
        Write time to RTC

        :param      time:       The time to set the RTC
        :type       time:       Union[str, List[int]]
        :param      time_type:  The type of time to change
        :type       time_type:  str

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        if (len(args) + len(kwargs) == 1):
            # only a time is given
            if len(args):
                time = args[0]
            else:
                time = kwargs["time"]
            if isinstance(time, str) and len(time) >= 19:
                # "2016,11,25,12,34,50"
                year = time[0:4]
                month = time[5:7]
                day = time[8:10]
                hour = time[11:13]
                minute = time[14:16]
                second = time[17:19]
            elif (isinstance(time, list) and
                  all(isinstance(x, int) for x in time)):
                # [2016, 11, 25, 12, 34, 50]
                year = time[0]
                month = time[1]
                day = time[2]
                hour = time[3]
                minute = time[4]
                second = time[5]
            else:
                raise NexRtcError("Time can either be given as '{}' or '{}'".
                                  format("2016,11,25,12,34,50",
                                         [2016, 11, 25, 12, 34, 50]))

            self._nh._logger.debug("Timestamp (ISO8601): {}-{}-{}T{}:{}:{}".
                                   format(year, month, day, hour, minute,
                                          second))

            cmd = "rtc0={}".format(year)
            self._nh.sendCommand(cmd)
            self._nh.recvRetCommandFinished()

            cmd = "rtc1={}".format(month)
            self._nh.sendCommand(cmd)
            self._nh.recvRetCommandFinished()

            cmd = "rtc2={}".format(day)
            self._nh.sendCommand(cmd)
            self._nh.recvRetCommandFinished()

            cmd = "rtc3={}".format(hour)
            self._nh.sendCommand(cmd)
            self._nh.recvRetCommandFinished()

            cmd = "rtc4={}".format(minute)
            self._nh.sendCommand(cmd)
            self._nh.recvRetCommandFinished()

            cmd = "rtc5={}".format(second)
            self._nh.sendCommand(cmd)
            return self._nh.recvRetCommandFinished()
        elif (len(args) + len(kwargs) == 2):
            # time_type is given as well
            if len(kwargs) == 2:
                time_type = kwargs['time_type']
                time = kwargs['time']
            else:
                if len(args) == 2:
                    time_type = args[0]
                    time = args[1]
                else:
                    raise NexRtcError("Either use keyword or positional args")

            self._nh._logger.debug("Set '{}' to '{}'".format(time_type, time))
            rtc_index = self.time_types.index(time_type.lower())

            cmd = "rtc{}={}".format(rtc_index, time)
            self._nh.sendCommand(cmd)
            return self._nh.recvRetCommandFinished()
        else:
            raise NexRtcError("Only two args are allowed")

    def read_rtc_time(self,
                      return_type: str,
                      length: Optional[int] = 22) -> Union[str, List[int]]:
        """
        Read RTC time

        :param      return_type:  The return type, choose "int", "str" or from
                                  ["year", "mon", "day", "hour", "min", "sec",
                                   "week"]
        :type       return_type:  str
        :param      length:       The length
        :type       length:       Optional[int]

        :returns:   RTC time
        :rtype:     Union[str, List[int]]
        """
        return_type = return_type.lower()

        if return_type in ["str", "int"]:
            cmd = "get rtc0"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            year = self._nh.recvRetNumber()

            cmd = "get rtc1"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            month = self._nh.recvRetNumber()

            cmd = "get rtc2"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            day = self._nh.recvRetNumber()

            cmd = "get rtc3"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            hour = self._nh.recvRetNumber()

            cmd = "get rtc4"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            minute = self._nh.recvRetNumber()

            cmd = "get rtc5"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            second = self._nh.recvRetNumber()

            cmd = "get rtc6"
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            week = self._nh.recvRetNumber()

            time_buf = [year, month, day, hour, minute, second, week]

            if return_type == "str":
                time_string = ("{}/{}/{} {}:{}:{} {}".
                               format(year, month, day, hour, minute, second,
                                      week))
                if length >= 22:
                    return time_string
                else:
                    return time_string[0:length]
            elif return_type == "int":
                if length >= 7:
                    return time_buf
                else:
                    return time_buf[0:length]
        elif return_type in self.time_types:
            rtc_index = self.time_types.index(return_type)
            cmd = "get rtc{}".format(rtc_index)
            self._nh.sendCommand(cmd)
            sleep(0.1)  # necessary, data might not be available otherwise
            return self._nh.recvRetNumber()
        else:
            raise NexRtcError("RTC time can only be returned as '{}' or '{}'"
                              "or chosen from {}".
                              format("str", "int", self.time_types))
