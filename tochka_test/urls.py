"""tochka_test URL Configuration

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
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.api import add, ping, substract, status

urlpatterns = [
    re_path(r'admin', admin.site.urls),
    re_path(r'api/ping/?$', csrf_exempt(ping), name='ping'),
    re_path(r'api/add/?$', csrf_exempt(add), name='add'),
    re_path(r'api/substract/?$', csrf_exempt(substract), name='substract'),
    re_path(r'api/status/?$', csrf_exempt(status), name='status'),
]
