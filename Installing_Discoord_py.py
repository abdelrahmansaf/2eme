#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
clear
echo "Installing base packages"
sudo apt-get install --yes git git-extras python3-pip
echo "Installing Discord"
sudo snap install discord
echo "Installing Visual studio code "
sudo snap install code
