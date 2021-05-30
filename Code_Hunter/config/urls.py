from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('quests/', include('wanted.urls')),
    path('community/', include('community.urls')),
    path('hunters/', include('search.urls')),
    path('', include('accounts.urls')),
]