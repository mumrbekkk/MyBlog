from ..repository.comments_repository import create_comment

def create_comment_from_form(comment_form, post, user):
    create_comment(
        text=comment_form.cleaned_data['text'],
        post=post,
        user=user
    )
