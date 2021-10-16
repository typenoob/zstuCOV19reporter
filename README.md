# zstuCOV19reporter

## 2021/10/16 有效的浙江理工大学健康打卡sh脚本v2.0

***重要！***

***为满足crontab定时运行脚本的需要，代码所有文件均是绝对路径，需要你自己修改***

***v2.0升级 必看！！！***

***增加页面失效检测***

***注释掉文件robot.py的第34行和42行以启用***

- 以js为核心
- 通过python3编写，基于selenium的webdriver
- 默认浏览器为ChromeDriver

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

**余下的操作需返回原来终端进行**

## 进入工作文件夹

```bash
cd zstuCOV19reporter

```

## 配置个人文件

~~#### 爬取健康申报原生网页（只需一次）~~
#### 我发现这个链接好像每个人通用的，可以直接使用我上传的link.save中的链接

1. 浏览器输入地址 stu.zstu.edu.cn
2. 登录你的账号
3. 点击便捷服务->健康申报-PC，点击健康申报按钮
4. 右键检查
5. 按下ctr+f 输入 搜索元素 iframe
6. 复制高亮元素的src值（双引号内）
7. 浏览器输入地址stu.zstu.edu.cn/ 在后面粘贴上刚才复制的值，访问成功后保存该地址作为你的健康申报的原生网页地址

#### 输入账号和密码
终端运行

```bash
python3 config.py
```

## 开始运行

#### 直接运行（只运行一次，不能保证成功，不推荐✖）

```bash
python3 robot.py
```

#### 脚本运行（运行直到成功 p.s. 最多五次，只要项目未失效就大概率不会失败，推荐✔）

```bash
./run.sh

```

## 日志信息

#### 存储路径

./log

#### 存储格式

$year-$month-$day.png

#### 注意⚠️

由于每天成功运行都会产生填报成功的截图，必要时请自行清理空间

## 新增

#### 通过对比验证打卡是否成功

基于pillow模块，robot.py在完成打卡的同时会比较当天打卡完成的截图与以往的是否相同，如果相同会输出“successful！”，如果不通会输出“error！”

## 更新计划

- 增加邮件订阅服务，当脚本运行失败时发送提醒⏰邮件
