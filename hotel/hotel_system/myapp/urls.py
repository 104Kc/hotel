from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),  # หน้าห้องพัก
     path("login/", views.login_view, name="login"), 
    path('booking-list/', views.booking_list, name='booking_list'),  # URL สำหรับรายการจอง
     path("register/", views.register, name="register"),
]
