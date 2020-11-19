"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from teamslide import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contact, name='contact'),
    path('contact/submitted=True',views.name_members, name='num_members'),
    path('contact/num_members/0',views.list_members,name='list_members'),
    path('contact/num_members/<int:numb>',views.name_members, name='num_members'),
    # url(r'^(?P<pid>[0-9]+)/$', 'info', name='members-info'),
   
    # path(r'^contact/\d+/',views.name_members,name='num_members'),
    # path(r'contact/<int:numb>/',views.name_members,name='num_members'),
    # path('contact/?submitted=True',views.name_members, name='num_members'),
    path('', RedirectView.as_view(url='contact/',permanent=True)),
]
