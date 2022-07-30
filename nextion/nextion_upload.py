#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
NexUpload

Functions to download TFT file to Nextion display
"""

# system packages
from os import listdir, stat
from time import sleep, ticks_diff, ticks_ms

# custom packages
from .common import Common


class NexUploadError(Exception):
    """Base class for exceptions in this module."""
    pass


class NexUpload(Common):
    """docstring for NexUpload"""
    def __init__(self, nh, file_name: str, download_baudrate: int) -> None:
        """
        Init upload

        :param      nh:                 The Nextion hardware interface object
        :type       nh:                 NexHardware
        :param      file_name:          The update filename
        :type       file_name:          str
        :param      download_baudrate:  The download baudrate
        :type       download_baudrate:  int
        """
        super().__init__(nh, pid=-1, cid=-1, name="upload")

        self._file_name = file_name
        self._file_size = 0
        self._download_baudrate = download_baudrate

        if not self._checkFile():
            raise NexUploadError("No such update file found: '{}'".
                                 format(file_name))

    @property
    def file_name(self) -> str:
        """
        Get the update filename

        :returns:   Filename of update file
        :rtype:     str
        """
        return self._file_name

    @property
    def file_size(self) -> int:
        """
        Get the update filesize

        :returns:   Filesize of update file in bytes
        :rtype:     int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, value: int) -> None:
        """
        Filesize of update file

        :param      value:  The filesize
        :type       value:  int
        """
        self._file_size = value

    @property
    def download_baudrate(self) -> int:
        """
        Get the download baudrate

        :returns:   Download baudrate for communication with Nextion display
        :rtype:     int
        """
        return self._download_baudrate

    @download_baudrate.setter
    def download_baudrate(self, value: int) -> None:
        """
        Set download baudrate

        :param      value:  The baudrate value
        :type       value:  int
        """
        self._download_baudrate = value

    def upload(self) -> bool:
        """
        Perform update of Nextion display content

        :returns:   True on success, raise NexUploadError otherwise
        :rtype:     bool
        """
        if not self._checkFile():
            raise NexUploadError("File not found")

        if self._getBaudrate() == 0:
            raise NexUploadError("Get baudrate error")

        if not self._setDownloadBaudrate(self.download_baudrate):
            raise NexUploadError("Modify baudrate error")

        if not self._downloadTftFile():
            raise NexUploadError("Download file error")

        self._nh._logger.debug("Download ok")
        return True

    def _checkFile(self) -> bool:
        """
        Check existance of specified TFT file

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        result = False
        if self._exists(self.file_name):
            # https://docs.python.org/3/library/os.html#os.stat
            info = stat(self.file_name)
            self.file_size = info[6]
            self._nh._logger.debug("TFT file size is '{}' bytes".
                                   format(self.file_size))
            self._nh._logger.debug("File check ok")
            result = True
        else:
            self._nh._logger.debug("File '{}' does not exist".
                                   format(self.file_name))
        return result

    def _getBaudrate(self) -> int:
        """
        Get communication baudrate with Nextion display

        :returns:   The baudrate
        :rtype:     int
        """
        baudrate_array = [115200, 19200, 9600, 57600, 38400, 4800, 2400]
        _baudrate = 0

        for baudrate in baudrate_array:
            self._nh._logger.debug("Checking connection with '{}' baud".
                                   format(baudrate))

            if self._searchBaudrate(baudrate):
                _baudrate = baudrate
                self._nh._logger.debug("Success, baudrate set to '{}' baud".
                                       format(_baudrate))
                return _baudrate

        return _baudrate

    def _searchBaudrate(self, baudrate: int) -> bool:
        """
        Find suitable download baudrate

        :param      baudrate:  The baudrate
        :type       baudrate:  int

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        self._nh._baudrate = baudrate
        self._nh._uart_init()
        self._nh.sendCommand("")
        self._nh.sendCommand("connect")
        sleep(0.1)  # necessary, data might not be available otherwise
        response = self._recvRetString()
        self._nh._logger.debug("_searchBaudrate response for '{}' baud: {}".
                               format(baudrate, response))

        if "comok" in response:
            return True

        return False

    def _setDownloadBaudrate(self, baudrate: int) -> bool:
        """
        Set the download baudrate

        :param      baudrate:  The baudrate
        :type       baudrate:  int

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        cmd = "whmi-wri {},{},0".format(self.file_size, baudrate)
        self._nh._logger.debug("Set download baudrate cmd: '{}'".format(cmd))

        self._nh.sendCommand("")
        self._nh.sendCommand(cmd)
        sleep(0.05)
        self._nh._baudrate = baudrate
        self._nh._uart_init()
        response = self._recvRetString(500)
        self._nh._logger.debug("Set download baudrate response: '{}'".
                               format(response))
        if (0x05).to_bytes(1, 'little') in response:
            return True
        return False

    def _downloadTftFile(self) -> bool:
        """
        Download TFT file to Nextion display

        :returns:   True on success, False otherwise
        :rtype:     bool
        """
        # send chunks of 4096
        file_content = bytearray(4096)

        with open(self.file_name, 'rb') as update_file:
            while True:
                data_size = update_file.readinto(file_content)

                if not data_size:
                    self._nh._logger.debug("Reached EOF, update finished")
                    break

                self._nh._uart.write(file_content)

                response = self._recvRetString(500)
                # self._nh._logger.debug("File download response: '{}'".
                #                        format(response))

                if (0x05).to_bytes(1, 'little') in response:
                    # send next chunk
                    pass
                else:
                    return False

        return True

    def _recvRetString(self, timeout: int = 100) -> bytearray:
        """
        Receive a string

        :param      timeout:  The communication timeout
        :type       timeout:  int

        :returns:   Received response
        :rtype:     bytearray
        """
        buf = bytearray(70)
        start_ms = ticks_ms()

        # stay inside this while loop at least for the timeout time
        while (ticks_diff(ticks_ms(), start_ms) <= timeout):
            # check amount of available characters
            while self._nh._uart.any():
                # can not decode received data here, as it might not be UTF-8
                self._nh._uart.readinto(buf)

        return buf

    def _exists(self, path: str) -> bool:
        """
        Check existance of file at given path.

        :param      path:   The path to the file
        :type       path:   str

        :returns:   Existance of file
        :rtype:     bool
        """
        result = False

        path_to_file_list = path.split('/')
        # ['path', 'to', 'some', 'file.txt']

        root_path = ''
        this_path = root_path

        for ele in path_to_file_list[:-1]:
            files_in_dir = listdir(this_path)
            # print('Files in {}: {}'.format(this_path, files_in_dir))

            if ele in files_in_dir:
                # print('"{}" found in "{}"'.format(ele, files_in_dir))

                if this_path == '':
                    this_path += '{}'.format(ele)
                else:
                    this_path += '/{}'.format(ele)

                # print('Next folder to be checked is: {}'.format(this_path))
            else:
                return result

        files_in_dir = listdir(this_path)
        if path_to_file_list[-1] in files_in_dir:
            # print('File "{}" found in "{}"'.
            #       format(path_to_file_list[-1], this_path))
            return True
        else:
            return False
