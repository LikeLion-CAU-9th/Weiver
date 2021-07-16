from django.contrib import admin
from .models import QuestComment, Quest, Review

admin.site.register(Quest)
admin.site.register(QuestComment)
admin.site.register(Review)

