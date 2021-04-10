"""K3Lh_project URL Configuration

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
from django.urls import path

from K3Lh_website.views import login, home, serbaserbi, pendataan, p3k, hasil, profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('serbaserbi/', serbaserbi, name = 'serbaserbi'),
    path('pendataan/', pendataan, name = 'pendataan'),
    path('p3k/', p3k, name = 'p3k'),
    path('hasil/', hasil, name = 'hasil'),
    path('profil/', profil, name = 'profil'),
]
