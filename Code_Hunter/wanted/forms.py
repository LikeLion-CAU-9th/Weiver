from django import forms
from .models import QuestComment, Review
from .models import Quest
from django_summernote.widgets import SummernoteWidget
 
class DateInput(forms.DateInput):
    input_type = 'date'

class CommentForm(forms.ModelForm):
    class Meta:
        model = QuestComment
        fields = ['author', 'body']

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'bounty', 'body', 'code', 'duedate', 'taglist', 'file']
        widgets = {
            'body': SummernoteWidget(),
            'duedate': DateInput(attrs={'placeholder':'마감기한'}),
            'file': forms.FileInput()
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'code', 'file']
        widgets = {
            'body': SummernoteWidget(),
            'file': forms.FileInput()
        }