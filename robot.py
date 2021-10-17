from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from PIL import Image
import math
import operator
import os
from functools import reduce
class Robot:
    def compare(self,pic1,pic2):
        image1 = Image.open(pic1)
        image2 = Image.open(pic2)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))
        return differ
    def __init__(self,workdir):
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--no-sandbox')
        opt.add_argument('disable-dev-shm-usage')
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)
        js = open('{path}/login.js'.format(path=workdir), 'r').read()
        self.browser.get('http://stu.zstu.edu.cn/webroot/decision/login')
        self.browser.execute_script(js)
        time.sleep(1)
        link = open('{path}/link.save'.format(path=workdir), 'r').read()
        self.browser.get(link)
        js = open('{path}/auto.js'.format(path=workdir), 'r').read()
        time.sleep(1)
        html=self.browser.find_element_by_class_name('x-table').get_attribute('innerText')
        open('{path}/log/right.html'.format(path=workdir),'w').write(html)
        if html[0:-14] != open('{path}/log/right.html'.format(path=workdir),'r').read()[0:-14]:
            print('invalid!!!')
            self.browser.quit()
            return
        self.browser.execute_script(js)
        time.sleep(5)
        path='{path}/log/'.format(path=workdir)+str(datetime.date.today())+'.png'
        self.browser.get_screenshot_as_file(path)
        self.browser.get_screenshot_as_file('{path}/log/right.png'.format(path=workdir))
        if self.compare(path,'{path}/log/right.png'.format(path=workdir))==0.0:
            print('successful!')
        else:
            print('error...')
        self.browser.quit()

robot=Robot(os.environ['zstuPATH'])
