from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, CommunityComment
from django.utils import timezone
from django.urls import reverse
from .forms import CommunityCommentForm
import datetime

def community(request):
    communities = Community.objects.all().order_by('-notice_or_not', '-pub_date')
    date_now = datetime.datetime.now().date()
    # date_communities = Community.objects.values('pub_dateonly').order_by('-notice_or_not', '-pub_date')
    return render(request,'community.html', {'communities': communities, 'date_now':date_now})

def create(request):
    new_post = Community()
    new_post.title = request.POST['title']
    new_post.author = "익명"
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.now()
    new_post.tag = request.POST['tag']
    if new_post.tag == '공지':
        new_post.notice_or_not = True
        new_post.author = "관리자"
    if datetime.datetime.now().date() == new_post.pub_date.date():
        new_post.today_or_not = True
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

def editPost(request, id):
    edit_post = Community.objects.get(id = id)
    return render(request, 'editPost.html', {'post': edit_post})

def updatePost(request, id):
    update_post = Community.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.author = "익명"
    update_post.body = request.POST['body']
    update_post.tag = request.POST['tag']
    update_post.pub_date = timezone.now()
    if update_post.tag == '공지':
        update_post.notice_or_not = True
        update_post.author = "관리자"
    if datetime.datetime.now().date() == update_post.pub_date.date():
        update_post.today_or_not = True
    update_post.save()
    return redirect('detail', update_post.id)

def deletePost(request, id):
    delete_post = Community.objects.get(id = id)
    delete_post.delete()
    return redirect('community')