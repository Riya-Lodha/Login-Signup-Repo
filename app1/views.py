from django.shortcuts import render, redirect
from django.contrib.auth.models import User #This import is of User table that is present in admin panel.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def home_page(request):
    return render(request, "home.html")

def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=user_name, password=pass1)
        if user:
            login(request, user)
            return redirect("home")
    return render (request, "login.html")

def signup_page(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        new_user = User.objects.create_user(user_name, user_email, pass1)
        new_user.save()
        return redirect("login")
    #Pick these variables from signup Form and then insert these into Models that are present in admin panel.

    return render (request, "signup.html")

def logout_page(request):
    logout(request)
    return redirect("login")
