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
        self.browser.get('http://stu.zstu.edu.cn//webroot/decision/view/report?viewlet=%252Fyewubanli%252F%25E5%2581%25A5%25E5%25BA%25B7%25E7%2594%25B3%25E6%258A%25A5.cpt&__parameters__=%257B%2522__pi__%2522%253Atrue%252C%2522op%2522%253A%2522write%2522%252C%2522_replaceview_%2522%253A%2522true%2522%252C%2522fine_hyperlink%2522%253A%2522b7892a31-9277-41fa-8469-b0cb95c8bb69%2522%257D&_=1634113351559&width=1608&height=610')
        js = open('auto.js', 'r').read()
        time.sleep(1)
        self.browser.execute_script(js)
        time.sleep(5)
        self.browser.get_screenshot_as_file('./result.png')
robot=Robot()
