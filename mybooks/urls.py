"""mybooks URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from books import views
from django.views.static import serve
from django.views.generic.base import RedirectView
from django.conf import settings
urlpatterns = [
    path('', views.index, name="index"),
    path('s/', views.search, name='search'),#搜索列表页
    path('clist/<int:lid>/', views.clist, name='clist'),#列表页
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')), 
    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#这里添加图片显示
]
