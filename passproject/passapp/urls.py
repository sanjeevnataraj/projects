from django.conf.urls import url,include
from django.contrib import admin
from passapp import views
urlpatterns = [
    url(r'^register/',views.register,name="register"),
    url(r'^login/',views.user_login,name="login"),
]
