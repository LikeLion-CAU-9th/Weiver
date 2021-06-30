from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Quest, QuestComment
from .forms import QuestForm, CommentForm
from django.urls import reverse
import datetime

def board(request):
    quests = Quest.objects.all().order_by('-id')
    for quest in quests:
        quest.remainingdays = (quest.duedate - datetime.datetime.now().date()).days
        quest.save()
    return render(request,'board.html', {'quests':quests})

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
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id','').strip()
        body = request.POST.get('body','').strip()
        author = request.POST.get('author','').strip()
        comment = QuestComment.objects.create(
            author = author,
            quest_id = quest_id,
            body = body
        )
        return redirect(reverse('questdetail', kwargs={'quest_id':comment.quest_id}))

def createquest(request):
    if request.method == 'POST':
        form = QuestForm(request.POST, request.FILES)
        print(dict(request.POST))
        if form.is_valid():
            quest = form.save(commit=False)
            quest.save()
            form.save_m2m()

            return redirect('board')
        else:
            print('error')
            return redirect('board')
    else:
        form = QuestForm()
        return render(request, 'newquest.html', {'form':form})


def matching(request):
    return render(request, 'matching.html', )


        