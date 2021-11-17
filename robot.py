# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from PIL import Image
import math
import operator
import sys
from functools import reduce
from selenium.webdriver.common.by import By


class Robot:
    def compare(self, pic1, pic2):
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(reduce(operator.add, list(
            map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))
        return differ

    def __init__(self):
        try:
            opt = Options()
            opt.add_argument('--headless')
            opt.add_argument('--disable-gpu')
            opt.add_argument('--no-sandbox')
            opt.add_argument('disable-dev-shm-usage')
            self.browser = webdriver.Chrome(options=opt)
            self.browser.implicitly_wait(30)
            js = open('./login.js', 'r',).read()
            self.browser.get('http://stu.zstu.edu.cn/webroot/decision/login')
            self.browser.execute_script(js)
            time.sleep(1)
            link = open('./link.save', 'r').read()
            self.browser.get(link)
            js = open('./auto.js', 'r').read()
            time.sleep(1)
            htmlpath = './log/' + str(datetime.date.today())+'.html'
            html = self.browser.find_element(By.CLASS_NAME,
                                             'x-table').get_attribute('innerText')
            open(htmlpath, 'w').write(html)
            if html[0:-14] != open('./log/right.html', 'r').read()[0:-14]:
                print('页面检验不成功（确认程序未失效可更新界面）')
                self.browser.quit()
                return
            self.browser.execute_script(js)
            time.sleep(5)
            picpath = './log/' + str(datetime.date.today())+'.png'
            self.browser.get_screenshot_as_file(picpath)
            if self.compare(picpath, './log/right.png') == 0.0:
                print('successful!')
            else:
                print('图片检验不成功（确认程序未失效可更新界面）')
        finally:
            self.browser.quit()


robot = Robot()
