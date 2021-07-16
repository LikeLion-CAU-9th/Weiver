from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import CommunityCommentForm
from .models import Community, CommunityComment
import datetime

def community(request):
    communities = Community.objects.all().order_by('-notice_or_not', '-pub_date')
    paginator = Paginator(communities, 16)
    page = request.GET.get('page')
    if page == None: 
        page = 1
    paginate_range, start_page, end_page = make_pagination_range(page, paginator)
    communities = paginator.get_page(page)
    # print("page is ", page)
    date_now = datetime.datetime.now().date()
    return render(request,'community.html', {'communities': communities, 'date_now':date_now, 'p_range' : paginate_range, 'start_page': start_page, 'end_page': end_page,})

def make_pagination_range(current_page, paginator):
    # pagination 10단위로 만들어주는 funtion
    if int(current_page) % 10 == 0:
        page_decimal = int(current_page) // 10 - 1
    elif int(current_page) % 10 != 0:
        page_decimal = int(current_page) // 10
    start_page = page_decimal * 10 + 1
    end_page = page_decimal * 10 + 10
    if end_page > paginator.num_pages:
        return range(start_page, paginator.num_pages + 1), start_page, end_page
    else:
        return range(start_page, end_page + 1), start_page, end_page

def create(request):
    new_post = Community()
    new_post.title = request.POST['title']
    new_post.author = request.user
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
            author = request.user,
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