"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_app import views
from django.conf.urls import url

# 匹配样式
urlpatterns = [
    # 默认自带 http://ip:port/admin/
    # 参数1：正则匹配规则
    # 参数2：视图函数
    path('admin/', admin.site.urls),
    # 自定义
    url(r'^hello', views.hello),
    url(r'^index', views.index),
    # 自定义 student 此时使用 include 包含其他的url文件
    url(r'^student/', include('django_app.urls')),
]
