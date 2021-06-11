from django.shortcuts import redirect, render, get_object_or_404
from .models import Quest, QuestComment
from .forms import CommentForm
from django.urls import reverse

def board(request):
    quests = Quest.objects.all().order_by('-id')
    return render(request,'board.html', {'quests':quests})

def sort_date(request):
    quests = Quest.objects.all().order_by('-id')
    return render(request,'board.html', {'quests':quests})

def sort_bounty(request):
    quests = Quest.objects.all().order_by('-bounty')
    return render(request,'board.html', {'quests':quests})

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



        