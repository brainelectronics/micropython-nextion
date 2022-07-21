#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from setuptools import setup
import pathlib
import sdist_upip

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# load elements of version.py
exec(open(here / 'nextion' / 'version.py').read())

setup(
    name='micropython-nextion',
    version=__version__,
    description="MicroPython Nextion serial displays library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brainelectronics/micropython-nextion',
    author=__author__,
    author_email='info@brainelectronics.de',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='micropython, nextion, display, nextion-display, nextion-communication, uart, library',
    project_urls={
        'Bug Reports': 'https://github.com/brainelectronics/micropython-nextion/issues',
        'Source': 'https://github.com/brainelectronics/micropython-nextion',
    },
    license='MIT',
    cmdclass={'sdist': sdist_upip.sdist},
    packages=['nextion'],
    install_requires=['micropython-ulogging']
)
