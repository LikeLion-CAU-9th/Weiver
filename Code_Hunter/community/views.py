from django.shortcuts import render, redirect, get_object_or_404
from .models import Community
from django.utils import timezone
import datetime

def community(request):
    communities = Community.objects.all().order_by('-id')
    # for community in communities:
    #     if (datetime.datetime.now().date() - community.pub_date.date()).days > 0:
    #         community.date_or_time = True
    #     elif (datetime.datetime.now().date() - community.pub_date.date()).days == 0: 
    #         community.date_or_time = False
    return render(request,'community.html', {'communities': communities})

def create(request):
    new_post = Community()
    new_post.title = request.POST['title']
    new_post.author = "익명"
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.now()
    new_post.save()

    return redirect('detail', new_post.id)

def detail(request, post_id):
    post_detail = get_object_or_404(Community, pk=post_id)
    return render(request,'detail.html', {'post_details': post_detail})

def newpost(request):
    return render(request, 'createpost.html')