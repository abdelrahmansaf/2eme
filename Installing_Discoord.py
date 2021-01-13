import os
print("UBUNTU POST-INSTALL SCRIPT")
print("Updating APT...")
#installing base package
os.system("sudo apt-get update")
#sudo apt-get update
os.system ("clear")
print("Installing base packages")
os.system ("sudo aptget install --yes git git-extras build-essentials python3-pip htop glances")
print("installing discord")
os.system ("sudo snap install discord")
os.system("snap refresh")
print("install code --classic")
os.system ("sudo snap install code --classic")
