from django.db import models
from . import post_model
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField(max_length=400)
    post = models.ForeignKey(post_model.Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)

    # def __str__(self):
    #     return self.user.username