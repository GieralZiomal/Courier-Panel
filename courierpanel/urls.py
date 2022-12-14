"""courierpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('login_view/', views.login_view, name="login_view"),
    path('login/', views.login, name="login"),
    path('register_view/', views.register_view, name="register_view"),
    path('register/', views.register, name="register"),
    path('pickpage/', views.pickpage, name="pickpage"),
    path('documents/', views.documents_view, name="documents"),
    path('senddocuments/', views.senddocuments, name="sdocuments"),
    path('changeinfo/', views.changeinfo, name="changeinfo"),
    path('changeinfo_view/', views.changeinfo_view, name="changeinfo_view"),
    path('earncharts/', views.earn_view, name="earncharts"),
    path('logout/', views.logout_view   , name="logout"),
    path('addinfo_view/', views.addinfo_view, name="addinfo_view"),
    path('addinfo/', views.addinfo, name="addinfo"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
