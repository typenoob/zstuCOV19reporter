from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from PIL import Image
import math
import operator
from functools import reduce
class Robot:
    def compare(self,pic1,pic2):
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))
        return differ
    def __init__(self):
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--no-sandbox')
        opt.add_argument('disable-dev-shm-usage')
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)
        js = open('/root/zstuCOV19reporter/login.js', 'r').read()
        self.browser.get('http://stu.zstu.edu.cn/webroot/decision/login')
        self.browser.execute_script(js)
        time.sleep(1)
        link = open('/root/zstuCOV19reporter/link.save', 'r').read()
        self.browser.get(link)
        js = open('/root/zstuCOV19reporter/auto.js', 'r').read()
        time.sleep(1)
        open('./log/right.html', 'w',encoding = "utf-8").write(self.browser.execute_script("return document.documentElement.outerHTML"))
        self.browser.execute_script(js)
        time.sleep(5)
        path='/root/zstuCOV19reporter/log/'+str(datetime.date.today())+'.png'
        self.browser.get_screenshot_as_file(path)
        if self.compare(path,'/root/zstuCOV19reporter/log/right.png')==0.0:
            print('successful!')
        else:
            print('error...')
        self.browser.quit()

robot=Robot()
