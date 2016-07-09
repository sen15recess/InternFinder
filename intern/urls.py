"""intern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1 import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^login/$', views.init_login, name ='init_login'),
    url(r'^admin/', admin.site.urls),
    url(r'^signin/$',views.login_view,name='login'),
    url(r'^initregister/$',views.register,name='initRegister'),
    url(r'^register/$',views.register_view,name='register'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^$',views.home,name='home'),
]
