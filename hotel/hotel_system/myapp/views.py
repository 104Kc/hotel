from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, "index.html")
def room(request):
    return render(request, 'room.html')
def login_view(request):
    if request.method == 'POST':
        # เขียนโค้ดตรวจสอบชื่อผู้ใช้และรหัสผ่านที่นี่
        return redirect('home')  # ถ้าล็อกอินสำเร็จจะไปหน้า index
    return render(request, 'login.html')
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})
def register(request):
    return render(request, 'register.html')
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "ชื่อผู้ใช้นี้ถูกใช้ไปแล้ว!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ")
        return redirect("login")  # ให้ลิงก์ไปหน้า login.html

    return render(request, "register.html")