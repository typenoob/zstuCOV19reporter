#! /bin/bash
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
read -p "请输入用户名(为空加载上次配置)：" user
if [ $user ]
then
        sed -i "1s/=.*/=$user/" login.js
else
        echo "加载上次配置"
fi
read -p "请输入密码(为空加载上次配置)：" password
if [ $password ]
then
        sed -i "2s/=.*/=\"$password\"/" login.js
else
        echo "加载上次配置"
fi
read -p "请输入工作目录(/path/zstuCOV19reporter)(为空不修改):" path
if [ $path ]
then
        echo zstuPATH=$path >> /etc/profile
        source /etc/profile
else
        echo "不修改"
fi
