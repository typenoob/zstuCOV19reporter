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
        echo "export zstuPATH=$path" >> /etc/profile
        source /etc/profile
else
        echo "不修改"
fi
