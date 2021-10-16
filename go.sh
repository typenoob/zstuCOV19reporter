#! /bin/bash
echo "正在安装依赖..."
sudo apt-get update
sudo apt-get install -y git
git clone https://github.com/typenoob/zstuCOV19reporter
cd zstuCOV19reporter
chmod +x run.sh
sudo apt-get install -y libxss1 libappindicator1 libindicator7 unzip xvfb libxi6 libgconf-2-4
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
pip3 install selenium
pip3 install pillow
sudo apt-get install -y chromium-browser
wget http://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
sudo rm chromedriver_linux64.zip
echo "依赖安装完成，开始个人信息配置..."
bash config.sh
echo "个人信息配置完成，请自行启动chromedriver"


