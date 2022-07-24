#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Update version info in python version file with latest changelog version

The changelog and package version shall always be aligned. This script can be
used to update the version info line "__version_info__ = ..." of a version.py
file with the latest changelog entry.
This changelog entry shall follow the semantic version pattern, see
https://semver.org/ and shall match the following pattern:

## [x.y.z] - yyyy-mm-dd

The line shall start with two hashtags followed by a single space. The semver
with x, y and z as non-negative integers, seperated by a dot and surrounded by
square brackets. Followed by a space, a dash, another space and the ISO8601
formatted date. Additional timestamps after the data, seperated from the date
by a single space, are optional.
"""

__author__ = "brainelectronics"
__copyright__ = "MIT License, Copyright (c) 2022 brainelectronics"
__credits__ = ["brainelectronics"]
__version__ = "0.1.0"
__maintainer__ = "brainelectronics"
__email__ = "git@brainelectronics.de"
__status__ = "Beta"

import argparse
import fileinput
import logging
from pathlib import Path
import re
import semver
from sys import stdout


def parser_valid_file(parser: argparse.ArgumentParser, arg: str) -> str:
    """
    Determine whether file exists.
    :param      parser:                 The parser
    :type       parser:                 parser object
    :param      arg:                    The file to check
    :type       arg:                    str
    :raise      argparse.ArgumentError: Argument is not a file
    :returns:   Input file path, parser error is thrown otherwise.
    :rtype:     str
    """
    if not Path(arg).is_file():
        parser.error("The file {} does not exist!".format(arg))
    else:
        return arg


def parse_arguments() -> argparse.Namespace:
    """
    Parse CLI arguments.
    :raise      argparse.ArgumentError  Argparse error
    :return:    argparse object
    """
    parser = argparse.ArgumentParser(description="""
    Update version info file based on changelog entry
    """, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # default arguments
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Output logger messages to stderr')

    # specific arguments
    parser.add_argument('--changelog_file',
                        dest='changelog_file',
                        required=True,
                        type=lambda x: parser_valid_file(parser, x),
                        help='Path to changelog file')

    parser.add_argument('--version_file',
                        dest='version_file',
                        required=True,
                        type=lambda x: parser_valid_file(parser, x),
                        help='Path to version file')

    parsed_args = parser.parse_args()

    return parsed_args


def parse_changelog(changelog_file: Path, logger: logging.Logger) -> str:
    """
    Parse the changelog for the first matching release version line

    :param      changelog_file:  The path to the changelog file
    :type       changelog_file:  Path
    :param      logger:          Logger object
    :type       logger:          logging.Logger

    :returns:   Extracted semantic version string
    :rtype:     str
    """
    release_version_line_regex = r"^\#\# \[\d{1,}[.]\d{1,}[.]\d{1,}\] \- \d{4}\-\d{2}-\d{2}"
    # append "$" to match only ISO8601 dates without additional timestamps
    release_version_line = ""

    with open(changelog_file, "r") as f:
        for line in f:
            match = re.search(release_version_line_regex, line)
            if match:
                release_version_line = match.group()
                break

    logger.debug("First matching release version line: '{}'".
                 format(release_version_line))

    return parse_semver_line(release_version_line, logger)


def parse_semver_line(release_version_line: str,
                      logger: logging.Logger) -> str:
    """
    Parse a release version line for a semantic version

    :param      release_version_line:  The release version line as described
    :type       release_version_line:  str
    :param      logger:                Logger object
    :type       logger:                logging.Logger

    :returns:   Semantic version string
    :rtype:     str
    """
    # release_version_line = "## [0.2.0] - 2022-05-19"
    semver_regex = r"\[\d{1,}[.]\d{1,}[.]\d{1,}\]"
    semver_string = "0.0.0"

    # extract semver from release version line
    match = re.search(semver_regex, release_version_line)
    if match:
        semver_string = match.group()
        # remove '[' and ']' from semver_string
        semver_string = re.sub(r"[\[\]]", "", semver_string)
        if not semver.VersionInfo.isvalid(semver_string):
            logger.error("Parsed SemVer string is invalid, check format")
            raise ValueError("Invalid SemVer string")
        logger.debug("Extracted SemVer string: '{}'".format(semver_string))
    else:
        logger.warning("No SemVer string found in given release version line")

    # semver_string = "0.2.0"
    return semver_string


def create_version_info_line(semver_string: str,
                             logger: logging.Logger) -> str:
    """
    Create the version info line used in "version.py"

    :param      semver_string:  The valid semver string
    :type       semver_string:  str
    :param      logger:         Logger object
    :type       logger:         logging.Logger

    :returns:   Complete version info line
    :rtype:     str
    """
    # semver_string = "0.2.0"
    ver = semver.VersionInfo.parse(semver_string)

    version_info = (str(ver.major), str(ver.minor), str(ver.patch))
    version_info_line = "__version_info__ = {}".format(version_info)
    logger.debug("New version info line: '{}'".format(version_info_line))

    # version_info_line = "__version_info__ = ('0', '2', '0')"
    return version_info_line


def update_version_file(version_file: Path,
                        version_info_line: str,
                        logger: logging.Logger) -> None:
    """
    Update the version file with a new version info line

    :param      version_file:       The path to the version file
    :type       version_file:       Path
    :param      version_info_line:  The version info line
    :type       version_info_line:  str
    :param      logger:             Logger object
    :type       logger:             logging.Logger
    """
    # standard output (print) is redirected to the original file
    for line in fileinput.input(version_file, inplace=True):
        if line.startswith("__version_info__ = "):
            print(version_info_line, end="\n")
        else:
            # keep line ending
            print(line, end="")

    logger.debug("Version file '{}' updated with '{}'".
                 format(version_file, version_info_line))


def main():
    # parse CLI arguments
    args = parse_arguments()

    custom_format = '[%(asctime)s] [%(levelname)-8s] [%(filename)-15s @'\
                    ' %(funcName)-15s:%(lineno)4s] %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=custom_format,
                        stream=stdout)
    logger = logging.getLogger(__name__)
    if args.debug:
        logger.setLevel(logging.DEBUG)

    here = Path(__file__).parent
    changelog_file = (here / args.changelog_file).resolve()
    version_file = (here / args.version_file).resolve()

    logger.debug("Using changelog file '{}' to update version file '{}'".
                 format(changelog_file, version_file))

    semver_string = parse_changelog(changelog_file, logger)
    version_info_line = create_version_info_line(semver_string, logger)
    update_version_file(version_file, version_info_line, logger)


if __name__ == '__main__':
    main()
