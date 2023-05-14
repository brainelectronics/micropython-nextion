## Examples Overview

| Example                   | Nextion name  | Supported          |
| ------------------------- | ------------- | ------------------ |
| [Button](button)          | NexButton     | :heavy_check_mark: |
| [Checkbox](checkbox)      | NexCheckbox   | :heavy_check_mark: |
| [Crop](crop)              | NexCrop       | :x:                |
| [DualButton](dual_button) | NexDual       | :heavy_check_mark: |
| [Gauge](gauge)            | NexGauge      | :heavy_check_mark: |
| [Gpio](gpio)              | NexGpio       | :heavy_check_mark: |
| [Hardware](hardware)      | NexHardware   | :heavy_check_mark: |
| [Hotspot](hotspot)        | NexHotspot    | :x:                |
| [Number](number)          | NexNumber     | :heavy_check_mark: |
| [Page](page)              | NexPage       | :heavy_check_mark: |
| [Picture](picture)        | NexPicture    | :x:                |
| [Progress](progress)      | NexProgress   | :heavy_check_mark: |
| [Radio](radio)            | NexRadio      | :heavy_check_mark: |
| [Rtc](rtc)                | NexRtc        | :heavy_check_mark: |
| [Scrolltext](scrolltext)  | NexScrolltext | :x:                |
| [Slider](slider)          | NexSlider     | :heavy_check_mark: |
| [Text](text)              | NexText       | :heavy_check_mark: |
| [Timer](timer)            | NexTimer      | :x:                |
| [Touch](touch)            | NexTouch      | :x:                |
| [Upload](upload)          | NexUpload     | :heavy_check_mark: |
| [Variable](variable)      | NexVariable   | :heavy_check_mark: |
| [waveform](waveform)      | NexWaveform   | :heavy_check_mark: |

<!-- https://www.webfx.com/tools/emoji-cheat-sheet/ -->

## Basic example

The [basic example](basic/main.py) shows the usage of all supported Nextion
elements by simple UART command calls.

The provided examples are designed for an **ESP32**.

Check [MicroPython UART documentation](https://docs.micropython.org/en/latest/library/machine.UART.html)
and the device/port specific setup for further details.

On a RP2 the RX and TX pin needs to be defined as e.g. `tx_pin = Pin(4)`,
`rx_pin = Pin(5)` and `uart_id = 1` whereas an ESP32 can use any pin with e.g.
`tx_pin = 21` and `rx_pin = 22` and `uart_id = 1`.

The following example code provides a universal RX/TX pin and UART ID setup.

```python
tx_pin = 21
rx_pin = 22
uart_id = 1

try:
    from machine import Pin
    import os
    from umodbus import version

    os_info = os.uname()
    print('MicroPython infos: {}'.format(os_info))
    print('Used micropthon-modbus version: {}'.format(version.__version__))

    if 'pyboard' in os_info:
        # NOT YET TESTED !
        # https://docs.micropython.org/en/latest/library/pyb.UART.html#pyb-uart
        # (TX, RX) = (X9, X10) = (PB6, PB7)
        tx_pin = Pin(PB6)
        rx_pin = Pin(PB7)
        uart_id = 1
    elif 'esp8266' in os_info:
        # NOT YET TESTED !
        # https://docs.micropython.org/en/latest/esp8266/quickref.html#uart-serial-bus
        raise Exception(
            'UART0 of ESP8266 is used by REPL, UART1 can only be used for TX'
        )
    elif 'esp32' in os_info:
        # https://docs.micropython.org/en/latest/esp32/quickref.html#uart-serial-bus
        tx_pin = 21
        rx_pin = 22
        uart_id = 1
    elif 'rp2' in os_info:
        # https://docs.micropython.org/en/latest/rp2/quickref.html#uart-serial-bus
        uart_id = 1
        tx_pin = Pin(4)
        rx_pin = Pin(5)
except AttributeError:
    pass
except Exception as e:
    raise e

nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin, uart_id=uart_id)
```

## Hardware example

The [hardware example](hardware/main.py) shows the usage of the hardware
functions `sleep`, `brightness` and `reset`.

## Upload example

The [upload example](upload/main.py) shows how to update a Nextion display
with a new TFT file.

Copy the [example TFT file](everything.tft) to the MicroPython board with
e.g. `rshell`

```bash
rshell --port /dev/tty.SLAB_USBtoUART --editor nano
```

Copy the file to the device, this might take several minutes!

```bash
cp everything.tft /pyboard
```
