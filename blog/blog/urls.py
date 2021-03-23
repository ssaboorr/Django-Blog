"""blog URL Configuration

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
from post import views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pv.home,name='home'),
    path('login/', pv.user_login, name='login'),
    path('logout/', pv.user_logout, name='logout'),
    path('dashboard/', pv.dashboard, name='dashboard'),
    path('signup/', pv.user_register, name='signup'),
    path('add/', pv.addpost, name='addpost'),
    path('update/<int:id>', pv.updatepost, name='update'),
    path('delete/<int:id>', pv.deletepost, name='delete'),

]
