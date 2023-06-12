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

### Install package

Connect the MicroPython device to a network (if possible)

```python
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('SSID', 'PASSWORD')
station.isconnected()
```

#### General

Install the latest package version of this lib on the MicroPython device

```python
import mip
mip.install("github:brainelectronics/micropython-nextion")
```

For MicroPython versions below 1.19.1 use the `upip` package instead of `mip`

```python
import upip
upip.install('micropython-nextion')
```

#### Specific version

Install a specific, fixed package version of this lib on the MicroPython device

```python
import mip
# install a verions of a specific branch
mip.install("github:brainelectronics/micropython-nextion", version="feature/add-mip-package-file")
# install a tag version
mip.install("github:brainelectronics/micropython-nextion", version="0.15.0")
```

For MicroPython versions below 1.19.1 use the `upip` package instead of `mip`

```python
import upip
upip.install('micropython-nextion')
```

#### Test version

Install a specific release candidate version uploaded to
[Test Python Package Index](https://test.pypi.org/) on every PR on the
MicroPython device. If no specific version is set, the latest stable version
will be used.

```python
import mip
mip.install("github:brainelectronics/micropython-nextion", version="0.15.0-rc1.dev29")
```

For MicroPython versions below 1.19.1 use the `upip` package instead of `mip`

```python
import upip
# overwrite index_urls to only take artifacts from test.pypi.org
upip.index_urls = ['https://test.pypi.org/pypi']
upip.install('micropython-nextion')
```

See also [brainelectronics Test PyPi Server in Docker][ref-brainelectronics-test-pypiserver]
for a test PyPi server running on Docker.

### Manually

#### Upload files to board

Copy the module to the MicroPython board and import them as shown below
using [Remote MicroPython shell][ref-remote-upy-shell]

Open the remote shell with the following command. Additionally use `-b 115200`
in case no CP210x is used but a CH34x.

```bash
rshell --port /dev/tty.SLAB_USBtoUART --editor nano
```

Perform the following command inside the `rshell` to copy all files and
folders to the device

```bash
mkdir /pyboard/lib
mkdir /pyboard/lib/nextion

cp nextion/* /pyboard/lib/nextion

cp examples/basic/main.py /pyboard
cp examples/boot.py /pyboard
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
[ref-brainelectronics-test-pypiserver]: https://github.com/brainelectronics/test-pypiserver
[ref-github-be-mircopython-modules]: https://github.com/brainelectronics/micropython-modules
[ref-itead-github]: https://github.com/itead
