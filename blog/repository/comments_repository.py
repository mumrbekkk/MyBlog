from ..models.comment_model import Comment


def create_comment(**kwargs):
    return Comment.objects.create(**kwargs)
    

