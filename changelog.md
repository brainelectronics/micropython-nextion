# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [x.y.z] - yyyy-mm-dd
### Added
### Changed
### Removed
### Fixed
-->

## Released
## [0.3.0] - 2022-07-22
### Added
- Function `hide()` and `show()` for all supported Nextion elements to hide
  or show the element on the screen
- Example how to hide and show an element in
  [hardware example](examples/hardware/main.py)

## [0.2.0] - 2022-07-21
### Added
- `brightness(value)` to [`nextion_hardware`](nextion/nextion_hardware.py) to
  control the display brightness
- `sleep(state)` to [`nextion_hardware`](nextion/nextion_hardware.py) to set
  display into sleep mode or wake it up
- `reset()` to [`nextion_hardware`](nextion/nextion_hardware.py) to reset the
  display to its default view like after a power cycle
- [Hardware example](examples/hardware) to show usage of new hardware functions

### Fixed
- Invalid pin usage in [`boot_wifi.py`](examples/boot_wifi.py) file

## [0.1.0] - 2022-07-21
### Added
- This changelog file
- [`.gitignore`](.gitignore) file
- [`.flake8`](.flake8) file
- [`setup.py`](setup.py) and [`sdist_upip.py`](sdist_upip.py) files for PyPi
  package creation and deploy
- [`LICENSE`](LICENSE) file
- [`requirements.txt`](requirements.txt) file to setup tools for board
  interactions
- [`README`](README.md) file with usage instructions
- Initial [`nextion`](nextion) library with basic element function support
- Example [`boot.py`](examples/boot.py) and
  [`boot_wifi.py`](examples/boot_wifi.py) files
- [Examples](examples) for all [supported Nextion elements](examples/README.md)
- [Example HMI file](examples/everything.HMI) to be used for all examples

<!-- Links -->
[Unreleased]: https://github.com/brainelectronics/micropython-nextion/compare/0.3.0...develop

[0.3.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.3.0
[0.2.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.2.0
[0.1.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.1.0

<!--
[ref-issue-1]: https://github.com/brainelectronics/micropython-nextion/issues/1
-->
