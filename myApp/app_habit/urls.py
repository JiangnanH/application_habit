from django.contrib import admin
from django.urls import path
from . import views

app_name = 'habit'
urlpatterns = [
    path('', views.home, name='Home'),
    path('addhabit/', views.add_habit, name='add_habit'),
    path('submithabit/', views.submit_habit, name='submit_habit'),
    path('<int:question_id>/', views.detail, name='detail'),
]
