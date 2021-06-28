from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', community, name="community"),
    path('newpost/', newpost, name = "newpost"),
    path('create/', create, name="create"),
    path('<int:post_id>/', detail, name="detail"),
]