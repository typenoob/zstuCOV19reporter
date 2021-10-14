# zstuCOV19report

## 2021/10/13 有效的浙江理工大学健康打卡sh脚本

- 以js为核心
- 通过python3编写，基于selenium的webdriver
- 默认浏览器为ChromeDriver

## 一键安装脚本

#### 通过 wget 命令安装 via wget to install script

```bash
wget -N --no-check-certificate "https://raw.githubusercontent.com/typenoob/zstuCOV19reporter/master/go.sh" && chmod +x go.sh && ./go.sh

```

## 进入工作文件夹

```bash
cd zstuCOV19reporter

```

## 配置个人文件

#### 输入账号密码

```bash
vim login.js

```
替换username为你的学号
替换password为你的密码

#### 爬取健康申报原生网页（只需一次）

1. 浏览器输入地址 stu.zstu.edu.cn
2. 登录你的账号
3. 点击便捷服务->健康申报-PC，点击健康申报按钮
4. 右键检查
5. 按下ctr+f 输入 搜索元素
6. 复制高亮元素的src值（双引号内）
7. 浏览器输入地址stu.zstu.edu.cn/ 在后面粘贴上刚才复制的值，访问成功后保存该地址作为你的健康申报的原生网页地址

#### 输入你的地址

```bash
vim robot.py

```
替换your link为你健康申报原生网页的地址

## 开始运行

#### 直接运行（只运行一次，不能保证成功，不推荐✖）

```bash
python3 robot.py

```

#### 脚本运行（运行直到成功，只要项目未失效就不会失败，推荐✔）

```bash
bash run.sh

```

## 日志信息

#### 存储路径

./log

#### 存储格式

time.asctime().result.png

#### 注意⚠️

由于每次成功运行都会产生填报成功的截图，必要时请自行清理空间

## 更新计划

- 增加页面检查功能，自动检查项目是否失效，若已失效则停止运行
- 增加邮件订阅服务，当脚本运行失败时发送提醒⏰邮件
