#!/bin/bash
OSVER="0.27.4" # Change to latest version of OpenSesame
FAENZAVER=1
echo "Installing dependencies"
sudo apt-get install python-pygame python-qt4 python-qscintilla2 python-imaging python-serial python-numpy python-tk
echo "Downloading OpenSesame"
wget https://github.com/smathot/OpenSesame/archive/release/$OSVER.tar.gz
echo "Extracting OpenSesame"
tar xvfz $OSVER.tar.gz
echo "Removing OpenSesame archive"
rm $OSVER.tar.gz
echo "Downloading Faenza icons"
wget http://files.cogsci.nl/misc/faenza-icons-for-opensesame-$FAENZAVER.tar.gz
echo "Extracting Faenza icons"
tar xvfz faenza-icons-for-opensesame-$FAENZAVER.tar.gz
echo "Moving Faenza to OpenSesame folder"
mv Faenza OpenSesame-release-$OSVER/resources/theme/default/
echo "Removing Faenza archive"
rm faenza-icons-for-opensesame-$FAENZAVER.tar.gz
