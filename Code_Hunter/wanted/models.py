from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone
from taggit.managers import TaggableManager
import datetime

class Quest(models.Model):
    SHOW_TYPES = [
        ('PUBLIC', 'PUBLIC'),
        ('PRIVATE', 'PRIVATE'),
    ]
    TAGS = [
        ('PYTHON', 'PYTHON'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JS', 'JS'),
    ]
    STATUS = [
        ('UNSOLVED', 'UNSOLVED'),
        ('SOLVING', 'SOLVING'),
        ('SOLVED', 'SOLVED'),
    ]
    author = models.CharField(max_length=8, verbose_name='닉네임', default='익명')
    title = models.CharField(max_length=50, verbose_name='제목')
    date = models.DateTimeField(auto_now_add=True)
    show = models.CharField(max_length = 10, choices=SHOW_TYPES, default='PUBLIC', help_text="비공개 여부")
    taglist = TaggableManager(blank=True)
    bounty = models.IntegerField(verbose_name='현상금', default=0)
    duedate = models.DateField(verbose_name='마감기한', default=datetime.date.today)
    file = models.FileField(null=True, verbose_name='첨부파일', blank=True)
    body = models.TextField(verbose_name='내용')
    code = models.TextField(default='', blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='UNSOLVED')
    remainingdays = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class QuestComment(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='comments')
    author =  models.CharField(max_length=8)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name="review")
    title = models.CharField(max_length=50, verbose_name='제목')
    author = models.CharField(max_length=8)
    body = models.TextField(verbose_name='내용')
    code = models.TextField(default='')
    file = models.FileField(null=True, verbose_name='첨부파일', blank=True)
