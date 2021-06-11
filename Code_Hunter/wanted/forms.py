from django import forms
from .models import QuestComment
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = QuestComment
        fields = ['author', 'body']
