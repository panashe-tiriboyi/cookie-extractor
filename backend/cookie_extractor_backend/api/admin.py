from django.contrib import admin
from .models import Cookie
from .models import CookieDbTest

admin.site.register(Cookie)
admin.site.register(CookieDbTest)
