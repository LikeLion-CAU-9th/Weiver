from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', board, name="board"),
    path('sort-date/', sort_date, name='sort-date'),
    path('sort-bounty/', sort_bounty, name='sort-bounty'),
    path('newquest/', newquest, name="newquest"),
    path('<int:quest_id>/', questdetail, name="questdetail"),
    path('newcomment/', newcomment, name="newcomment"),
    path('createquest/', createquest, name="createquest"),
    path('<int:quest_id>/matching/', matching, name = "matching"),
    path('<int:quest_id>/select-reviewer/', select_reviewer, name="select-reviewer"),
    path('<int:quest_id>/review/', review, name="review"),
    path('<int:quest_id>/apply/', apply, name="apply"),
]
