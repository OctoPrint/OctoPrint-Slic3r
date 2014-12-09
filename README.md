# Slic3r plugin for OctoPrint

**WARNING** Not functional yet since slic3r's return codes are behaving unexpectedly. WIP for others to take a look at
and maybe build upon.

## Setup

Install the plugin like you would install any regular Python package from source:

    pip install https://github.com/OctoPrint/OctoPrint-Slic3r/archive/master.zip
    
Make sure you use the same Python environment that you installed OctoPrint under, otherwise the plugin
won't be able to satisfy its dependencies.

Restart OctoPrint. `octoprint.log` should show you that the plugin was successfully found and loaded:

    2014-10-29 12:29:21,500 - octoprint.plugin.core - INFO - Loading plugins from ... and installed plugin packages...
    2014-10-29 12:29:21,611 - octoprint.plugin.core - INFO - Found 2 plugin(s): Slic3r (0.1.0), Discovery (0.1)

## Configuration

TODO