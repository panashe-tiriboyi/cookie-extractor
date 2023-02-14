import requests
import os
import subprocess
import array
import json
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
from rest_framework import generics
from rest_framework import viewsets
from .serializers import CookieSerializer,DataBaseCookieSerializer, ClientDomainsSerializer, DomainSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .cookie_extractor import Extractor
import chromedriver_autoinstaller
from .models import Cookie
from .models import ClientDomains
from .models import Domain

chromedriver_autoinstaller.install()
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

def load_cookies(url):

        driver.execute_cdp_cmd('Network.enable', {})
    
        cookie = {'domain': url, 'httpOnly': False, 'name': 'CookieConsent', 'path': '/', 'secure': True, 'value': '{stamp:%27P3NBnLXzElYWnYjNPg0SIvUIaQ6u3PrN2rZOEj4bTA2i2u6ydMKcSw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1659611890724%2Cregion:%27no%27}', 'expires': 1691147890}    
    
            
            # Set the actual cookie
        driver.execute_cdp_cmd('Network.setCookie', cookie)
    
        # Disable network tracking
        driver.execute_cdp_cmd('Network.disable', {})
        return 1

@api_view(['GET','POST'])
def listcookies(request):

    cookies=[]
    # getting url from client side
    if request.method == 'POST':
        
      url = request.data['cookie_domain']
      print(f'================Posted domain is =====>{url}')


      load_cookies(url)
    #   'https://www.volvat.no'
      driver.get("https://"+url)

      cookies = driver.get_cookies()
    #   extractor script comes here

    #   res = requests.get(url)

      #print(list_object)
    
    
    # looping 
  

    cookie_list =[]

    for cookie in cookies:
        cookie_name = cookie['name']
        print(f'============>cookie name is {cookie_name}')
        cookie_id =cookie['path']
        cookie_value=cookie['value']
        cookie_expiration_date=cookie['domain']
        cookie_domain=cookie['domain']
        cookie_secure_flag=cookie['secure']
        cookie_http_only_flag=cookie['httpOnly']

        object = Extractor(cookie_name,cookie_id,cookie_value,cookie_expiration_date,cookie_domain,cookie_secure_flag,cookie_http_only_flag)
        cookie_list.append(object)

    # cookie = Extractor(test_id[12:],test_value,test_expires,test_domain,test_http_only,test_secure_flag)
    serializer_class = CookieSerializer(cookie_list,many=True)
    return Response(serializer_class.data)

class CookieList(generics.ListCreateAPIView):
  queryset = Cookie.objects.all()
  serializer_class = DataBaseCookieSerializer

class CookieDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cookie.objects.all()
  serializer_class = DataBaseCookieSerializer


class ClientDomainsDetails(viewsets.ReadOnlyModelViewSet):
    queryset = ClientDomains.objects.all()
    serializer_class = ClientDomainsSerializer

# @api_view(['GET', 'POST'])
# def listdomians(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     serializer_class = DomainSerializer(many=True)
#     return Response(serializer_class.data)

class DomainDetail(viewsets.ModelViewSet):
  serializer_class = DomainSerializer

  def get_queryset(self):
    domain = Domain.objects.all()
    return domain

  


