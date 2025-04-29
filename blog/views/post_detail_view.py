from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import View
from ..forms.comment_form import MyCommentForm
from ..repository.posts_repository import get_post_by_slug, get_post_comments, get_post_tags
from ..repository.session_repository import get_session_value
from ..service.comment_service import create_comment_from_form


class PostDetailView(View):
    def my_context(self, post, request, form):
        context = {
            'post': post, 
            'post_tags': post.tags.all(),
            'comments': get_post_comments(post).order_by("-id"),
            'comment_form': form,
            'stored_post_ids': get_session_value(request, 'stored_post_ids')
        }
        return context

    def get(self, request, slug):
        post = get_post_by_slug(slug)
        
        context = self.my_context(post, request, MyCommentForm())
        
        return render(request, "blog/post-detail.html", context)
    

    def post(self, request, slug):
        comment_form = MyCommentForm(request.POST)
        post = get_post_by_slug(slug)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                create_comment_from_form(comment_form, post, user=request.user)
                return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
            else:
                comment_form.add_error("text", "Log in to write a comment!")

        context = self.my_context(post, request, comment_form)
        
        return render(request, "blog/post-detail.html", context)
