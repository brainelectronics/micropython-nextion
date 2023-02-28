# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
sys.path.insert(0, os.path.abspath('../'))
here = Path(__file__).parent.resolve()

try:
    # Inject mock modules so that we can build the
    # documentation without having the real stuff available
    from mock import Mock

    to_be_mocked = [
        'micropython',
        'machine',
        'ulogging',
        'time.ticks_diff', 'time.ticks_ms',
    ]
    for module in to_be_mocked:
        sys.modules[module] = Mock()
        print("Mocked '{}' module".format(module))
    from nextion import common
except ImportError:
    raise SystemExit("nextion has to be importable")
else:
    pass

# load elements of version.py
exec(open(here / '..' / 'nextion' / 'version.py').read())

# -- Project information

project = 'micropython-nextion'
copyright = '2023, brainelectronics'
author = 'brainelectronics'

version = __version__
release = version

# -- General configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]
autosectionlabel_prefix_document = True

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
suppress_warnings = [
    # throws an error due to not found reference targets to files not in docs/
    'ref.myst',
    # throws an error due to multiple "Added" labels in "changelog.md"
    'autosectionlabel.*'
]

# A list of regular expressions that match URIs that should not be checked
# when doing a linkcheck build.
linkcheck_ignore = [
    # tag 0.14.0 did not exist during docs introduction
    'https://github.com/brainelectronics/micropython-nextion/tree/0.14.0',
    # RTD page did not exist during docs introduction
    'https://micropython-nextion.readthedocs.io/en/latest/',
]

templates_path = ['_templates']

# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
