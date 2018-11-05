from django.urls import path

from . import views

from django.contrib import admin

app_name = 'warehouse'

urlpatterns = [


    path('admin/', admin.site.urls)


]

