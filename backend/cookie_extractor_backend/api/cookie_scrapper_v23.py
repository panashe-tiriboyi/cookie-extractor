#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from urllib.parse import urlparse
from selenium.common.exceptions import WebDriverException
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import randrange
import time
import re
import os


# In[3]:


# Start Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-dev-tools')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--window-size=1280x1696')
options.add_argument('--user-data-dir=/tmp/chrome-user-data')
options.add_argument('--single-process')
options.add_argument("--no-zygote")
options.add_argument('--ignore-certificate-errors')


DRIVER_PATH = Service("chromedriver")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=DRIVER_PATH, options=options)



def load_cookies(url,driver):

        driver.execute_cdp_cmd('Network.enable', {})
    
        cookie = {'domain': 'www.volvat.no', 'httpOnly': False, 'name': 'CookieConsent', 'path': '/', 'secure': True, 'value': '{stamp:%27P3NBnLXzElYWnYjNPg0SIvUIaQ6u3PrN2rZOEj4bTA2i2u6ydMKcSw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1659611890724%2Cregion:%27no%27}', 'expires': 1691147890}    
    
            
            # Set the actual cookie
        driver.execute_cdp_cmd('Network.setCookie', cookie)
    
        # Disable network tracking
        driver.execute_cdp_cmd('Network.disable', {})
        driver.get(url)
        cookies=driver.get_cookies()
        
        return cookies


#driver.get('https://www.volvat.no')
#print(driver.get_cookies())


# In[9]:

url = input()
cookies=load_cookies(url,driver)


cookies