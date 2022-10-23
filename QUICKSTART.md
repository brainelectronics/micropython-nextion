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

### Install package on board with pip

```bash
rshell -p /dev/tty.SLAB_USBtoUART --editor nano
```

Inside the rshell

```bash
cp examples/progressbar/main.py /pyboard
cp examples/boot.py /pyboard
repl
```

Inside the REPL

```python
import machine
import network
import time
import upip

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('SSID', 'PASSWORD')
time.sleep(1)
print('Device connected to network: {}'.format(station.isconnected()))

upip.install('micropython-nextion')

print('Installation completed')
machine.soft_reset()
```

<!-- Links -->
[ref-upy-firmware-download]: https://micropython.org/download/
