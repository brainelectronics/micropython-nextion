# Examples

Usage examples of this `micropython-nextion` library

---------------

## General

An example of all implemented functionalities can be found at the
[MicroPython Nextion examples folder][ref-micropython-nextion-examples]

## Setup Nextion

```python
from nextion import NexHardware

# define communication pins for Nextion display
tx_pin = 21
rx_pin = 22

# create Nextion hardware interface
nh = NexHardware(rx_pin=rx_pin, tx_pin=tx_pin)

# init nextion communication interface
nh.nexInit()

# modify text field "t0" showing "newtxt" by default
cmd = 't0.txt="asdf"'
nh.sendCommand(cmd)
```

## Special hints

### Access object on a non active page

In order to modify an object on another page than the currently displayed one, prepend the page name to the object/component name.

The valid and working way could be

```python
# default way of accessing a Nextion Number object "n0" on page "0" with the
# component ID "1"
n0 = NexNumber(nh, 0, 1, "n0")

# assuming currently page3 is active
# activate the page of the desired Nextion Number object and set its value
page1.show()
n0.setValue(35)

# return to the previous page
page3.show()
```

A more elegant way of achieving the same result, see
[comment and solution of vahithosan][ref-modify-object-on-non-active-page]

```python
# access the Nextion Number object "n0" on page "0" with the component ID "1"
# from another page directly without showing the page first
n0 = NexNumber(nh, 0, 1, "page0.n0")

# assuming currently page3 is active
# activate the page of the desired Nextion Number object and set its value
n0.setValue(35)

# show page with already updated value
page1.show()
```

<!-- Links -->
[ref-micropython-nextion-examples]: https://github.com/brainelectronics/micropython-nextion/tree/develop/examples
[ref-modify-object-on-non-active-page]: https://github.com/brainelectronics/micropython-nextion/issues/20#issuecomment-1289640668
