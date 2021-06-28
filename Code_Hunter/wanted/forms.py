from django import forms
from .models import QuestComment
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
            'duedate': DateInput(),
        }

