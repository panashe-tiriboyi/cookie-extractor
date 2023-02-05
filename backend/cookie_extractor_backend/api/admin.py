from django.contrib import admin
from .models import Cookie
from .models import CookieDbTest
from .models import ClientDomains
from .models import Domain


admin.site.register(Cookie)
admin.site.register(CookieDbTest)
admin.site.register(ClientDomains)
admin.site.register(Domain)