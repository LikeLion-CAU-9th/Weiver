from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, CommunityComment
from django.utils import timezone
from django.urls import reverse
from .forms import CommunityCommentForm
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
    comments = CommunityComment.objects.filter(origin_post=post_detail.id)
    return render(request,'detail.html', {'post_details':post_detail, 'comments':comments})

def newpost(request):
    return render(request, 'createpost.html')

def new_comment(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id', '').strip()
        content = request.POST.get('comment-content', '').strip()
        comment = CommunityComment.objects.create(
            author = "익명",
            origin_post_id = post_id,
            content = content
        )
        return redirect(reverse('detail', kwargs = {"post_id":comment.origin_post_id}) )
