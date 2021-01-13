import os
print("UBUNTU POST-INSTALL SCRIPT")
#update the system
os.system("sudo apt-get update")
#installing base package
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")
print("dowloading discord")
os.system("wget -O discord.deb 'https://discordapp.com/api/download?platform=linux&format=deb'")
print("installing discord")
os.system("sudo dpkg -i /path/to/discord.deb")
os.system("snap refresh")
os.system("sudo snap install code --classic")
print("python3 installed")
print("Discord installed")
