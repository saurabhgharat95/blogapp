from django import forms
from .models import BlogComments

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ('blog_comment',)