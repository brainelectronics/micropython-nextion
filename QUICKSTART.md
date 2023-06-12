# MicroPython Nextion library

[![Downloads](https://pepy.tech/badge/micropython-nextion)](https://pepy.tech/project/micropython-nextion)
![Release](https://img.shields.io/github/v/release/brainelectronics/micropython-nextion?include_prereleases&color=success)
![MicroPython](https://img.shields.io/badge/micropython-Ok-green.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MicroPython Nextion library

---------------

## Get started

This is a quickstart guide to flash the
[MicroPython firmware][ref-upy-firmware-download], connect to a network and
install the MicroPython Nextion library on the board

### Flash firmware

```bash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART erase_flash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 921600 write_flash -z 0x1000 esp32spiram-20220117-v1.18.bin
```

### Install package

Connect the MicroPython device to a network (if possible)

```python
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('SSID', 'PASSWORD')
station.isconnected()
```

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

### Copy example file

Copy one of the provided example `main.py` files to the MicroPython device.

```bash
rshell --port /dev/tty.SLAB_USBtoUART --editor nano
```

Perform the following command inside the `rshell` to copy the Progressbar example to the MicroPython device.

```bash
cp examples/progressbar/main.py /pyboard
cp examples/boot.py /pyboard
repl
```

<!-- Links -->
[ref-upy-firmware-download]: https://micropython.org/download/
