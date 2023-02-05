from django.urls import path
from . import views
from .views import CookieList, CookieDetail, ClientDomainsDetails, DomainDetail

urlpatterns = [
path('', views.listcookies,name='CookieList'),
path('<int:pk>/', CookieDetail.as_view()),
path('db_cookies', CookieList.as_view()),
path('client_domains/',ClientDomainsDetails.as_view({'get': 'list'})),
path('domain', DomainDetail.as_view({'get': 'list'})),
]