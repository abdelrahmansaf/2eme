#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "installing discord"
sudo apt-get update
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
wget -O discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"
sudo dpkg -i /path/to/discord.deb
snap refresh
sudo snap install code --classic
echo "python3 installed"
echo "Discord installed"

