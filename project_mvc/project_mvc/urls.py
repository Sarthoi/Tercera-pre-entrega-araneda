"""
URL configuration for project_mvc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from project_mvc.views import *
from firstapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('motos/', motos, name='motos'),
    path('autos/', autos, name='autos'),
    path('users/', users, name='users'),
    path('getmotos/', getmotos, name='getmotos'),
    path('getautos/', getautos, name='getautos'),
    path('getusers/', getusers, name='getusers'),
    path('search_motos/', search_motos, name='search_motos'),
    path('search_autos/', search_autos, name='search_autos'),
    path('search_users/', search_users, name='search_users'),
]
