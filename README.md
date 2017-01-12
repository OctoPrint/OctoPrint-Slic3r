# Slic3r plugin for OctoPrint

**WARNING**

This plugin has been successfully tested for the following cases:</br>
1. Linux: Slic3r's stable versions 1.1.7 and 1.2.9 (tests done under a Raspberry Pi 2, but it should work for other Linux distributions).</br>
2. Windows: Slic3r works for version 1.2.9, not doing it for version 1.1.7.

## Setup

In order to install the plugin, go to Settings -> Plugin Manager and click on 'Get more...':

![Screenshot](http://imgur.com/9NaAl37.png)

You'll see an option to add it from an URL. Add https://github.com/javierma/OctoPrint-Slic3r/archive/master.zip an click on 'Install' button.

![Screenshot](http://i.imgur.com/lln2TvT.png)

At this moment, the plugin will be installed, but Slic3r must be downloaded and configured, which can be done following these steps:

1. If OctoPrint is running under a Raspberry Pi, you can use the following script to install Slic3r (unfortunately precompiled packages do not work for RPI's architecture). For that purpose, copy the following code in a file (i.e. slic3r_install.sh).

```
  #!/bin/sh

  echo "Shell script created by Javier Martínez Arrieta for Slic3r installation\n"
  #Ask the user for a version
  echo "Please indicate which version you desire to be installed (e.g. 1.1.7)"
  read version
  echo "The installation of Slic3r takes a long time. PLease be patient"
  cd $HOME
  echo "Installing required libraries and dependencies..."
  sudo apt-get install git libboost-system-dev libboost-thread-dev git-core build-essential libgtk2.0-dev libwxgtk2.8-dev libwx-perl libmodule-build-perl libnet-dbus-perl cpanminus libextutils-cbuilder-perl gcc-4.7 g++-4.7 libwx-perl libperl-dev
  sudo cpanm AAR/Boost-Geometry-Utils-0.06.tar.gz Math::Clipper Math::ConvexHull Math::ConvexHull::MonotoneChain Math::Geometry::Voronoi Math::PlanePath Moo IO::Scalar Class::XSAccessor Growl::GNTP XML::SAX::ExpatXS PAR::Packer
  echo "Cloning Slic3r repository..."
  git clone https://github.com/alexrj/Slic3r.git
  cd Slic3r
  git checkout $version
  echo "Building and testing Scli3r..."
  sudo perl Build.PL
  echo "If everything was installed properly,you should be able to run Slic3r with the command ./slic3r.pl"   
```

2. Save the file and allow execution giving permission. Using a terminal, it would be chmod +x slic3r_install.sh (or the name given t the file).
```
  chmod +x slic3r_install.sh
```
  
3. Now that you have permission to execute it, type ./slic3r_install.sh and press 'Enter'. If it is the first time executing the installer, take into account that it can take about 30 minutes or even more.
```
 ./slic3r_install.sh
```

4. At the beggining of the installation, you will be asked which version should be installed (available versions at http://slic3r.org/download)

  ![Screenshot](http://imgur.com/Qa2Dgv7.png)

5. Execute OctoPrint and go to Settings (or restart when you are asked after installing the plugin). Slic3r should appear in Plugins list:

  ![Screenshot](http://i.imgur.com/44yDsJ6.png)

6. In 'General', you should put the following path for the executable (supposing the execution of the script, the path would be /home/pi/Slic3r/slic3r.pl). <b>Note: If running in Windows, write the path to slic3r-console</b>:

  ![Screenshot](http://i.imgur.com/1ckQCgL.png)

7. Before importing the profile, you have to export a file with the Slic3r's configuration. For that purpose, open Slic3r, and select File-> Export Config...

  ![Screenshot](http://i.imgur.com/41XFyEI.png)

8. Save the file with the desired name (e.g. config.ini):

  ![Screenshot](http://imgur.com/YzfqRXM.png)

9. Once done, in 'Profiles' click 'Import Profile...' button:

  ![Screenshot](http://imgur.com/HkbO1G8.png)

10. Click on 'Browse...' and search for the profile. Once done, save with the name and identifier wished by clicking 'Confirm':

  ![Screenshot](http://i.imgur.com/7NJmJK3.png)

11. Click 'Save' to confirm Slic3r settings:

  ![Screenshot](http://imgur.com/HkbO1G8.png)

12. Now you can slice your stl files:

  ![Screenshot](http://i.imgur.com/AC1g0un.png)
