username=input('请输入学号（为空加载上次配置）')
if username:
    cmd='sed -i \'\'1s/=.*/='+username+'/g\'\' login.js'
    os.system(cmd)
password=input('请输入密码（为空加载上次配置）')
if password:
    password='"'+password+'"'
    cmd='sed -i \'\'2s/=.*/='+password+'/g\'\' login.js'
    os.system(cmd)
link=input('请输入链接（不能为空）')
