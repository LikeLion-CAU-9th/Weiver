from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils import timezone
import datetime
from accounts.models import CustomUser

# Create your models here.
class Community(models.Model):
    title = models.CharField(max_length=200, verbose_name= "제목")
    author = models.ForeignKey(CustomUser, verbose_name="작성자", on_delete = models.CASCADE, related_name="posts")
    pub_date = models.DateTimeField()
    pub_dateonly = models.DateField(default= datetime.date.today)
    body = models.TextField()
    votes = models.IntegerField(default= 0)
    views = models.IntegerField(default = 0)
    notice_or_not = models.BooleanField(default = False)
    tag = models.CharField(max_length=16, default="공지")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class CommunityComment(models.Model):
    author =  models.ForeignKey(CustomUser, verbose_name = "작성자", on_delete = models.CASCADE)
    content = models.TextField()
    pub_datetime = models.DateTimeField(auto_now_add=True)
    origin_post = models.ForeignKey(Community, on_delete=CASCADE, related_name= "comments")
    def __str__(self):
        return self.content[:20]

    