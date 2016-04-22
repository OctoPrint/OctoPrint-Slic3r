# Slic3r plugin for OctoPrint

This plugin has been successfully tested for Slicer's stable versions 1.1.7 and 1.2.9.

## Setup

In order to install the plugin, go to Settings -> Plugin Manager and click on 'Get more...':

![Screenshot](http://imgur.com/9NaAl37.png)

You'll see an option to add it from an URL. Add https://github.com/javierma/OctoPrint-Slic3r/archive/master.zip an click on 'Install' button.

![Screenshot](http://i.imgur.com/lln2TvT.png)

At this moment, the plugin will be installed, but Slic3r must be downloaded and configured, which can be done following these steps:

  -If OctoPrint is running under a Raspberry Pi, you can use the following script to install Slic3r (unfortunately precompiled packages do not work for RPI's architecture). For that purpose, copy the following code in a file (i.e. slic3r_install.sh).
  
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
  
  -Save the file and allow execution giving permission. Using a terminal, it would be chmod +x slic3r_install.sh (or the name given to the file).
  
  ![Screenshot](http://imgur.com/NRZkshW.png)
  
  -Now that you have permission to execute it, type ./slic3r_install.sh and press 'Enter'. If it is the first time executing the installer, take into account that it can take about 30 minutes or even more.

  ![Screenshot](http://imgur.com/nkbmWxL.png)

  -At the beggining of the installation, you will be asked which version should be installed (available versions at http://slic3r.org/download)

  ![Screenshot](http://imgur.com/Qa2Dgv7.png)

  -Execute OctoPrint and go to Settings (or restart when you are asked after installing the plugin). Slic3r should appear in Plugins list:

  ![Screenshot](http://i.imgur.com/44yDsJ6.png)

  -In 'General', you should put the following path for the executable: /home/pi/Slic3r/slic3r.pl:

  ![Screenshot](http://i.imgur.com/1ckQCgL.png)

  -Before importing the profile, you have to export a file with the Slic3r's configuration. For that purpose, open Slic3r, and select File-> Export Config...

  ![Screenshot](http://i.imgur.com/41XFyEI.png)

  -Save the file with the desired name (e.g. config.ini):

  ![Screenshot](http://imgur.com/YzfqRXM.png)

  -Once done, in 'Profiles' click 'Import Profile...' button:

  ![Screenshot](http://imgur.com/HkbO1G8.png)

  -Click on 'Browse...' and search for the profile. Once done, save with the name and identifier wished by clicking 'Confirm':

  ![Screenshot](http://i.imgur.com/7NJmJK3.png)

  -Click 'Save' to confirm Slic3r settings:

  ![Screenshot](http://imgur.com/HkbO1G8.png)

  -Now you can slice your stl files:

  ![Screenshot](http://i.imgur.com/AC1g0un.png)
