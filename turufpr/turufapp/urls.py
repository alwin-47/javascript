from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
path('',views.index,name='index'),
path('contact/',views.contact,name='contact'),
path('about/',views.about,name='about'),
path('booking/',views.booking,name='booking'),
path('turufs/',views.turufs,name='turufs'),


]
