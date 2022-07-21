# MicroPython Nextion library

[![Downloads](https://pepy.tech/badge/micropython-nextion)](https://pepy.tech/project/micropython-nextion)
![Release](https://img.shields.io/github/v/release/brainelectronics/micropython-nextion?include_prereleases&color=success)
![MicroPython](https://img.shields.io/badge/micropython-Ok-green.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MicroPython Nextion library

---------------

## General

Ported library to interact with [Nextion serial displays][ref-nextion-wiki],
based on the [ITEAD Arduino Nextion][ref-itead-nextion-github] library.

## Installation

### Install required tools

Python3 must be installed on your system. Check the current Python version
with the following command

```bash
python --version
python3 --version
```

Depending on which command `Python 3.x.y` (with x.y as some numbers) is
returned, use that command to proceed.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Setup

### Install package with upip

Connect the MicroPython device to a network (if possible)

```python
import network
station = network.WLAN(network.STA_IF)
station.connect('SSID', 'PASSWORD')
station.isconnected()
```

and install this lib on the MicroPython device like this

```python
import upip
upip.install('micropython-nextion')
```

### Manually

#### Upload files to board

Copy the module to the MicroPython board and import them as shown below
using [Remote MicroPython shell][ref-remote-upy-shell]

Open the remote shell with the following command. Additionally use `-b 115200`
in case no CP210x is used but a CH34x.

```bash
rshell --port /dev/tty.SLAB_USBtoUART --editor nano
```

Perform the following command to copy all files and folders to the device

```bash
mkdir /pyboard/lib
mkdir /pyboard/lib/nextion

cp nextion/* /pyboard/lib/nextion

cp examples/main.py /pyboard
cp examples/boot.py /pyboard
```

### Install additional MicroPython packages

To use this package with the provided [`boot.py`](examples/boot.py) and one of
the `main.py` files of an [example subfolder](examples/), the additional
module `ulogging` is required.

Either install the required package(s) using `upip` as follows after
connecting to a WiFi network:

```python
# network connection already established

import upip
upip.install('micropython-ulogging')
```

or copy it manually to the MicroPython board using e.g. `rshell`:

```bash
mkdir /pyboard/lib

cp -r libs_external/* /pyboard/lib
```

## Usage

Use one of the [examples](examples/) to get started. Read also the
[examples README](examples/README.md) to find all supported elements

## Credits

Big thank you to [ITEAD Studio][ref-itead-github] for the implementation
of the Arduino library.

<!-- Links -->
[ref-nextion-wiki]: https://wiki.iteadstudio.com/Nextion_HMI_Solution
[ref-itead-nextion-github]: https://github.com/itead/ITEADLIB_Arduino_Nextion
[ref-remote-upy-shell]: https://github.com/dhylands/rshell
[ref-github-be-mircopython-modules]: https://github.com/brainelectronics/micropython-modules
[ref-itead-github]: https://github.com/itead
