import os
from time import sleep

from Config.readconfig import xxreadini
from selenium import webdriver

#工程路径
parent_path = os.path.dirname(os.path.dirname(__file__))
#专门读取配置文件对象
xiaoxin = xxreadini()
#获取被测试网址
url=xiaoxin.get_value("url")

def get_chrome_driver():
    driver_path=parent_path+"/BrowserDriver/chromedriver"
    driver =webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return  driver

if __name__ == '__main__':
    get_chrome_driver()


