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
<!--
RegEx for release version from file
r"^\#\# \[\d{1,}[.]\d{1,}[.]\d{1,}\] \- \d{4}\-\d{2}-\d{2}$"
-->

## Released
## [0.11.0] - 2022-07-30
### Added
- Support `NexUpload` usage with [`nextion_upload`](nextion/nextion_upload.py)

## [0.10.0] - 2022-07-30
### Added
- Support `NexVariable` usage with
  [`nextion_variable`](nextion/nextion_variable.py)

### Fixed
- Add full line comment between different section of all examples

## [0.9.0] - 2022-07-30
### Added
- Support GPIO usage with [`nextion_gpio`](nextion/nextion_gpio.py)
- [Usage example](examples/gpio/main.py) of GPIO

## [0.8.0] - 2022-07-30
### Added
- Support all class specific functions of
    - Button
    - Dual state button
    - Number
    - Slider
    - Waveform

### Changed
- Add full line comment between different section of examples

### Fixed
- Flake8 warnings in several classes due to many imports and inheritance

## [0.7.1] - 2022-07-29
### Fixed
- Add class `CommonPointerMixin` to [`common`](nextion/common.py)

## [0.7.0] - 2022-07-29
### Added
- Support `Get_pointer_thickness_wid` and `Set_pointer_thickness_wid` by new
  class `CommonPointerMixin` in [`common`](nextion/common.py)

### Changed
- Inherit from `CommonPointerMixin` in
    - Gauge
    - Slider

## [0.6.0] - 2022-07-29
### Added
- Support `Get_place_xcen`, `Set_place_xcen`, `Get_place_ycen` and
  `Set_place_ycen` by new class `CommonPositionMixin` in
  [`common`](nextion/common.py)

### Changed
- Inherit from `CommonPositionMixin` in
    - Button
    - Dual state button
    - Number
    - Text

### Fixed
- Remove unused imports in nextion elements

## [0.5.0] - 2022-07-29
### Added
- Support `Get_background_color_bco` and `Set_background_color_bco` by new
  class `CommonBackgroundColorMixin` in [`common`](nextion/common.py)
- Support `Get_font_color_pco`, `Set_font_color_pco`, `getFont` and `setFont`
  by new class `CommonFontMixin` in [`common`](nextion/common.py)

### Changed
- Inherit from `CommonFontMixin` and `CommonBackgroundColorMixin` in
    - Button
    - Checkbox
    - Dual state button
    - Gauge
    - Number
    - Progressbar
    - Radio
    - Slider
    - Text
    - Waveform

### Fixed
- Remove unsupported `CommonValueMixin` from Button
- Some typos in comments

## [0.4.0] - 2022-07-24
### Added
- `clearChannel(channel)` in [`nextion_waveform`](nextion/nextion_waveform.py)
  to clear a waveform channel data
- Script to [update version file](update_version.py) based on changelog entry
- [Requirements file](requirements-deploy.txt) for GitHub CI python publish
  workflow
- [GitHub CI python publish workflow](.github/workflows/python-publish.yml)

### Fixed
- Replace undefined `__author__` in [`setup.py`](setup.py)
- Add missing shebang header to [`version`](nextion/version.py) file

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
[Unreleased]: https://github.com/brainelectronics/micropython-nextion/compare/0.11.0...develop

[0.11.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.11.0
[0.10.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.10.0
[0.9.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.9.0
[0.8.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.8.0
[0.7.1]: https://github.com/brainelectronics/micropython-nextion/tree/0.7.1
[0.7.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.7.0
[0.6.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.6.0
[0.5.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.5.0
[0.4.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.4.0
[0.3.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.3.0
[0.2.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.2.0
[0.1.0]: https://github.com/brainelectronics/micropython-nextion/tree/0.1.0

<!--
[ref-issue-1]: https://github.com/brainelectronics/micropython-nextion/issues/1
-->
