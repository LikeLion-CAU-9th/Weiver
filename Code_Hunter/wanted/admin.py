from django.contrib import admin
from .models import QuestComment, Quest

admin.site.register(Quest)
admin.site.register(QuestComment)

