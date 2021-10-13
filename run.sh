#! /bin/bash
python3 robot.py
while [ $? -ne 0 ]    # 判断程序上次运行是否正常结束
do
    echo "Process exits with errors! Restarting!"
    python3 robot.py    #重启程序
done
echo "Process ends!"