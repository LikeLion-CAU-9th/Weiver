from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils import timezone
import datetime

# Create your models here.
class Community(models.Model):
    title = models.CharField(max_length=200, verbose_name= "제목")
    author = models.CharField(max_length=20, verbose_name = "작성자", default = "익명")
    author_pic = models.ImageField(upload_to = "img/", blank = True, null = True)
    pub_date = models.DateTimeField()
    # pub_time = models.TimeField()
    body = models.TextField()
    votes = models.IntegerField(default= 0)
    views = models.IntegerField(default = 0)
    comment_count = models.IntegerField(default = 0)
    date_or_time = models.BooleanField(default= True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class CommunityComment(models.Model):
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    author = models.CharField(max_length=20, verbose_name="작성자", default= "익명")
    content = models.TextField()
    pub_datetime = models.DateTimeField()
    origin_post = models.ForeignKey(Community, on_delete=CASCADE)