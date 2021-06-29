from django import forms
from django.db.models import fields
from .models import CommunityComment, Community

class CommunityCommentForm(forms.ModelForm):
    class Meta :
        model = CommunityComment
        fields = ['content']