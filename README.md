# Slic3r plugin for OctoPrint

This is forked from the official version.  This fork doesn't assume a specific version of OctoPrint so it should be able to work with all versions of octoprint files.

## Setup

Install the plugin like you would install any regular Python package from source:

    pip install https://github.com/eyal0/OctoPrint-Slic3r/archive/master.zip
    
Make sure you use the same Python environment that you installed OctoPrint under, otherwise the plugin
won't be able to satisfy its dependencies.

Restart OctoPrint. `octoprint.log` should show you that the plugin was successfully found and loaded:

    2014-10-29 12:29:21,500 - octoprint.plugin.core - INFO - Loading plugins from ... and installed plugin packages...
    2014-10-29 12:29:21,611 - octoprint.plugin.core - INFO - Found 2 plugin(s): Slic3r (0.1.0), Discovery (0.1)
