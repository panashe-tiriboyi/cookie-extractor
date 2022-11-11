from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Compare ,CookieDbTest, CookieDbTest1, CookieDbTest2, CookieDbTest3, CookieDbTest4
import time


# Create your views here.

def index (requests):
    return HttpResponse(output)

def current_milli_time():
    return round(time.time() * 1000)

def Check(tableName):
    compare = Compare.objects.all()
    table= tableName.objects.all()
    a= 1


    t1 = current_milli_time()
    for c in table:
        for i in compare:
            if i.id_name == c.id_name :
                a= a +1
            else:
                a = a + 2

    diff = current_milli_time() - t1
    return diff 

output = f'{Check(CookieDbTest)}  {Check(CookieDbTest1)} {Check(CookieDbTest2)} {Check(CookieDbTest3)} {Check(CookieDbTest4)}'       


