from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
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
        self.browser.get('your link')
        js = open('auto.js', 'r').read()
        time.sleep(1)
        self.browser.execute_script(js)
        time.sleep(5)
        self.browser.get_screenshot_as_file('./log/'+time.asctime()+'result.png')
username=input()
password=input()
cmd='sed -i \'\'1s/=.*/='+username+'/g\'\' login.js'
cmd='sed -i \'\'2s/=.*/='+password+'/g\'\' login.js'
robot=Robot()
