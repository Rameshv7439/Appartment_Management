"""Appartment_Management_System URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Appartment_App import admin_urls,owner_urls,userr_urls
from Appartment_App.views import IndexView, AboutView, Owner_Reg, User_Reg, Login
from Appartment_Management_System import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',IndexView.as_view()),
    path('about',AboutView.as_view()),
    path('owner_reg',Owner_Reg.as_view()),
    path('user_reg',User_Reg.as_view()),
    path('admin/',admin_urls.urls()),
    path('owner/',owner_urls.urls()),
    path('userr/',userr_urls.urls()),
    path('login',Login.as_view())
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
