# Slic3r plugin for OctoPrint

**WARNING**

This plugin has been successfully tested for the following cases:

1. Linux: Slic3r's stable versions 1.1.7 and 1.2.9 (tests done under a Raspberry Pi 2, but it should work for other Linux distributions).
2. Linux: Also tested with [Slic3r Prusa Edition](https://github.com/prusa3d/Slic3r) version 1.33.8.  Versions >= 1.34 might work with TBB using [these instructions](https://github.com/OctoPrint/OctoPrint-Slic3r/wiki/How-to-install-Slic3r-on-RPi).
3. Windows: Slic3r works for version 1.2.9, not doing it for version 1.1.7.

Install using these instructions: https://github.com/OctoPrint/OctoPrint-Slic3r/wiki/How-to-install-Slic3r-on-RPi

## Setup

In order to install the plugin, go to Settings -> Plugin Manager and click on 'Get more...':

![Screenshot](http://imgur.com/9NaAl37.png)

You'll see an option to add it from an URL. Add https://github.com/OctoPrint/OctoPrint-Slic3r/archive/master.zip an click on 'Install' button.

![Screenshot](http://i.imgur.com/lln2TvT.png)

At this moment, the plugin will be installed, but Slic3r must be downloaded and configured, which can be done following these steps: https://github.com/OctoPrint/OctoPrint-Slic3r/wiki/How-to-install-Slic3r-on-RPi

1. Execute OctoPrint and go to Settings (or restart when you are asked after installing the plugin). Slic3r should appear in Plugins list:

   ![Screenshot](http://i.imgur.com/44yDsJ6.png)

2. In 'General', you should put the following path for the executable (supposing the execution of the script, the path would be /home/pi/Slic3r/slic3r.pl). <b>Note: If running in Windows, write the path to slic3r-console</b>:

   ![Screenshot](http://i.imgur.com/1ckQCgL.png)

3. Before importing the profile, you have to export a file with the Slic3r's configuration. For that purpose, open Slic3r, and select File-> Export Config...

   ![Screenshot](http://i.imgur.com/41XFyEI.png)

4. Save the file with the desired name (e.g. config.ini):

   ![Screenshot](http://imgur.com/YzfqRXM.png)

5. Once done, in 'Profiles' click 'Import Profile...' button:

    ![Screenshot](http://imgur.com/HkbO1G8.png)

6. Click on 'Browse...' and search for the profile. Once done, save with the name and identifier wished by clicking 'Confirm':

    ![Screenshot](http://i.imgur.com/7NJmJK3.png)

7. Click 'Save' to confirm Slic3r settings:

    ![Screenshot](http://imgur.com/HkbO1G8.png)

8. Now you can slice your stl files:

    ![Screenshot](http://i.imgur.com/AC1g0un.png)
