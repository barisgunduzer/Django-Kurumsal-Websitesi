"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from home import views

urlpatterns = [

    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

    path('iletisim/', views.iletisim, name='iletisim'),
    path('blog/', views.blog, name='blog'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslarimiz/', views.referanslar, name='referanslarimiz'),

    path('blog/<slug:slug>/<int:id>/', views.blog_detail, name='blog_detail'),

]

if settings.DEBUG: #new
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

