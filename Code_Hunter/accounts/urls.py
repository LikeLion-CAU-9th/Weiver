from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('my_page/', my_page, name="my_page"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
]