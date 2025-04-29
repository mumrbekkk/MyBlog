from django import forms
from ..models.comment_model import Comment


# Model Form Example
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }    
"""

class MyCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "write your comment here..."}))


    