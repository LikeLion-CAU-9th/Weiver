from django.shortcuts import render
from .models import Quest

def board(request):
    quests = Quest.objects.all().order_by('-id')
    return render(request,'board.html', {'quests':quests})