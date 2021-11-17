#! /bin/bash
source /etc/profile
cd /root/zstuCOV19reporter
count=0
stoped=5
result=`python3 robot.py`
while [[ ! $result == "successful!" ]]    # 判断程序上次运行是否正常结束
do
    echo "Process exits with errors! Restarting!"
    if [ $count == $stoped ]
    then
        echo "Process exits with errors! Can't autofix!"
	break
    else
	count=`expr $count + 1`
    fi
    result=`python3 robot.py`
done
echo $result|mail -s test 850683617@qq.com
