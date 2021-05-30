from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', community, name=""),
    path('create/', community, name=""),
    path('<int:post_id>/', detail, name="detail"),
]