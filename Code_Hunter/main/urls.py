from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('account_base', account_base, name = "aaaaa"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)