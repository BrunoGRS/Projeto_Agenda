from django.contrib import admin
from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('create/user/', views.register, name='create_user'),
    path('schedule/<int:contact_id>/delete/', views.delete, name='delete'),
    path('schedule/<int:contact_id>/update/', views.update, name='update'),
    path('schedule/create/', views.create_contact, name='create'),
    path('contact/<int:contact_id>/details/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
