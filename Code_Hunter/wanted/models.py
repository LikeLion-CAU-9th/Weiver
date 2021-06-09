from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField

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
    author = models.CharField(max_length=8, verbose_name='닉네임')
    title = models.CharField(max_length=50, verbose_name='제목')
    date = models.DateTimeField(auto_now_add=True )
    show = models.CharField(max_length = 10, choices=SHOW_TYPES, default='PUBLIC', help_text="비공개 여부")
    tags = MultiSelectField(choices=TAGS)
    bounty = models.IntegerField(verbose_name='현상금')
    deadline = models.DateField(verbose_name='마감기한')
    file = models.FileField(null=True, verbose_name='첨부파일')

    body = models.TextField(verbose_name='내용')

    def __str__(self):
        return self.title