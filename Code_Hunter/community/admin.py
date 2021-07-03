from django.contrib import admin
from .models import Community, CommunityComment

# Register your models here.
admin.site.register(Community)
admin.site.register(CommunityComment)