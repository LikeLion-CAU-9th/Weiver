from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', community, name="community"),
    path('newpost/', newpost, name = "newpost"),
    path('create/', create, name="create"),
    path('<int:post_id>/', detail, name="detail"),
    path('new_comment/', new_comment, name ="new_comment"),
    path('edit/<str:id>', editPost, name = "edit_post"),
    path('update/<str:id>', updatePost, name = "update_post"),
]