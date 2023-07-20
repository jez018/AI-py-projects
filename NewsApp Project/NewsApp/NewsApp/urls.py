"""NewsApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views
from .methods import getJsonNewsData, runner_first
from .TestFolder import api_test


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^testing/$', views.test),
    url(r'^test2/$', views.test2),
    url(r'^test101/$', runner_first.runner),
    url(r'^check/$', api_test.test101)
]
