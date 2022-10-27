from django.urls import path
from . import views
from .views import CookieList, CookieDetail

urlpatterns = [
path('', views.listcookies,name='CookieList'),
path('<int:pk>/', CookieDetail.as_view()),
path('db_cookies', CookieList.as_view()),

]