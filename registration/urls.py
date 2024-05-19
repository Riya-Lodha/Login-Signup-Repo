from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path("home/", views.home_page, name="home"),
    path("logout/", views.logout_page, name="logout"),
]
