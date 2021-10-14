from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def loadINFO():
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
class Robot:
    def __init__(self):
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--no-sandbox')
        opt.add_argument('disable-dev-shm-usage')
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)
        js = open('login.js', 'r').read()
        self.browser.get('http://stu.zstu.edu.cn/webroot/decision/login')
        self.browser.execute_script(js)
        time.sleep(1)
        self.browser.get(link)
        js = open('auto.js', 'r').read()
        time.sleep(1)
        self.browser.execute_script(js)
        time.sleep(5)
        self.browser.get_screenshot_as_file('./log/'+time.asctime()+'result.png')

loadINFO()
robot=Robot()
