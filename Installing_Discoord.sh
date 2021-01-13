#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
#update the system
sudo apt-get update
#installing base package
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
echo "dowloading discord"
wget -O discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"
echo "installing discord"
sudo dpkg -i /path/to/discord.deb
snap refresh
sudo snap install code --classic
echo "python3 installed"
echo "Discord installed"

