#!/bin/bash

# Add deadsnakes PPA and install the Python 3.13 available
echo "Adding deadsnakes PPA and installing Python 3.13..."
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13 python3.13-venv -y
echo "Installed python 3.13"

# Delete the old UbuntuVenv directory
echo "Deleting UbuntuVenv ... .."
rm -rf UbuntuVenv
echo "Deleted the old UbuntuVenv....."

# Create a new virtual environment named UbuntuVenv
echo "Creating new UbuntuVenv with Python 3.13....."
python3.13 -m venv UbuntuVenv
echo "Created new UbuntuVenv"

# Navigate to the bin directory of the virtual environment
echo "Navigating to the bin directory....."
cd UbuntuVenv/bin

# Activate the virtual environment
echo "Activating the UbuntuVenv....."
source ./activate
echo "Activated The UbuntuVenv....."

#Upgrade pip
echo "Upgrading pip....."
python3 -m pip install --upgrade pip
echo "pip Upgraded....."

# Install requirements from requirements.txt (assumes it's in ~/Desktop/ML_practice)
echo "Installing dependencies from requirements.txt....."
pip install -r ../../requirements.txt
echo "Dependencies installed successfully....."

# Return to the root directory (~/Desktop/ML_practice)
echo "Returning to the root directory....."
cd ../..
echo "Returned to the root Directory....."
echo "Now you can start....."
echo "Your Python Version is: $(python --version)"
