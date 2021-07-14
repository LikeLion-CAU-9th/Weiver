from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Quest, QuestComment, Review
from .forms import QuestForm, CommentForm, ReviewForm
from django.urls import reverse
import datetime

def board(request):
    page = request.GET.get('page', '1')
    quests = Quest.objects.filter(duedate__gte=datetime.datetime.now()).order_by('-id')
    for quest in quests:
        quest.remainingdays = (quest.duedate - datetime.datetime.now().date()).days
        quest.save()
    paginator = Paginator(quests, 6)
    currentpage = paginator.get_page(page)
    context = {'quests':currentpage}
    return render(request,'board.html', context)

def sort_date(request):
    quests = Quest.objects.all().order_by('-id')
    return render(request,'board.html', {'quests':quests})

def sort_bounty(request):
    quests = Quest.objects.all().order_by('-bounty')
    return render(request,'board.html', {'quests':quests})

def newquest(request):
    return render(request, 'newquest.html')

def questdetail(request, quest_id):
    quest_detail = get_object_or_404(Quest, pk=quest_id)
    comments = QuestComment.objects.filter(quest=quest_detail.id)
    return render(request, 'questdetail.html', context = {'quest':quest_detail, 'comments':comments})

def newcomment(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id','').strip()
        body = request.POST.get('body','').strip()
        author = request.user
        comment = QuestComment.objects.create(
            author = author,
            quest_id = quest_id,
            body = body
        )
        return redirect(reverse('questdetail', kwargs={'quest_id':comment.quest_id}))

def createquest(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        if form.is_valid():
            quest = form.save(commit=False)
            quest.author = request.user
            quest.save()
            form.save_m2m()
            return redirect('board')
        else:
            return redirect('board')
    else:
        form = QuestForm()
        return render(request, 'newquest.html', {'form':form})


def matching(request):
    return render(request, 'matching.html', )

def review(request, quest_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('board')
        else:
            return redirect('board')
    else:
        form = ReviewForm()
        quest_detail = get_object_or_404(Quest, pk=quest_id)
        context = {'quest':quest_detail, 'form':form}
        return render(request, 'createreview.html', context)
    
def apply(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    quest = get_object_or_404(Quest, pk=quest_id)
    return redirect('index')
    


        