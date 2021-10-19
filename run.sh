#! /bin/bash
source /etc/profile
count=0
stoped=5
result=`python3 $zstuPATH/robot.py`
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
    result=`python3 $zstuPATH/robot.py`
done
echo $result
