# zstuCOV19reporter

## 2021/10/16 有效的浙江理工大学健康打卡sh脚本v2.0

- 以js为核心
- 通过python3编写，基于selenium的webdriver
- 默认浏览器为ChromeDriver

---

***重要！***

***请确保开启chromedriver服务和输入个人信息（包括环境变量zstuPATH）后后再运行程序***

---

## ***v2.0升级 必看！！！***

#### ***增加页面失效检测***

1.手动运行一次核心程序(确保log目录下生成文件right.html和right.png)

```bash
python3 robot.py
```

2.注释掉文件robot.py的第34行和42行以启用功能

---

#### ***简化安装流程***

***请以root用户进行操作***

1.下载并运行安装脚本(过程中要输入学号密码信息，输入链接可以选择直接回车）


```bash
wget -N --no-check-certificate "https://raw.githubusercontent.com/typenoob/zstuCOV19reporter/master/go.sh" && chmod +x go.sh && ./go.sh

```

2.打开chromedriver服务（新开一个终端，或者通过screen保证其在后台运行）

```bash
chromedriver
```

3.添加环境变量(yourpath是你的路径)

```bash
echo "export zstuPATH=yourpath/zstuCOV19reporter" >> /etc/profile
source /etc/profile
```

4.增加页面失效检测（具体见上文，可选非必要但推荐）

5.运行命令开单次运行

```bash
report
```
6.服务器端通过crontab每天运行，详情见下文

## 一键安装脚本

#### 通过 wget 命令安装 via wget to install script

```bash
wget -N --no-check-certificate "https://raw.githubusercontent.com/typenoob/zstuCOV19reporter/master/go.sh" && chmod +x go.sh && ./go.sh

```

## 开启chromedriver服务

新键一个终端并执行以下命令

（ssh连接无法新建终端可以参考screen多开的方法 https://wxnacy.com/2017/12/21/screen/ ）

```bash
chromedriver

```

## 开始运行

#### 直接运行（只运行一次，不能保证成功，不推荐✖）

```bash
python3 $zstuPATH/robot.py
```

#### 脚本运行（运行直到成功 p.s. 最多五次，只要项目未失效就大概率不会失败，推荐✔）

```bash
$zstuPATH/run.sh

```

## 修改个人信息

```bash
bash $zstuPATH/config.sh

```

## 生成命令

```bash
cp $zstuPATH/run.sh /bin/report

```

## 服务器端运行（依赖crontab）

1.执行命令

```bash
crontab -e

```

2.在文件的末尾加入下面的语句，按下ctr+x->y->enter后保存退出（需要提前生成命令）

```
MAILTO=youremail@yourdomain.com
00 8 * * * report

```

3.执行命令

```bash
service cron restart

```

4.查看是否生效

```bash
crontab -l

```

## 日志信息

#### 存储路径

$zstuPATH/log

#### 存储格式

$year-$month-$day.png

#### 注意⚠️

由于每天成功运行都会产生填报成功的截图，必要时请自行清理空间

## 新增

#### 通过对比验证打卡是否成功

基于pillow模块，robot.py在完成打卡的同时会比较当天打卡完成的截图与以往的是否相同，如果相同会输出“successful！”，如果不同会输出“error！”

## 更新计划

- 增加邮件订阅服务，当脚本运行失败时发送提醒⏰邮件
