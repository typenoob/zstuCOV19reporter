#! /bin/bash
sudo apt-get update
sudo apt-get install -y git
git clone https://github.com/typenoob/zstuCOV19reporter
cd zstuCOV19reporter
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
pip3 install selemium
sudo apt-get install -y unzip
sudo apt-get install -y chromium-browser
wget http://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
sudo rm chromedriver_linux64.zip
