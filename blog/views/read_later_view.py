from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models.post_model import Post
from ..repository.session_repository import get_session_value


class ReadLaterView(View):
    def get(self, request):
        stored_post_ids = get_session_value(request, "stored_post_ids") or []
        posts = []
        if stored_post_ids:
            posts = Post.objects.filter(id__in=stored_post_ids)
        
        context = {"posts": posts}
        
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_post_ids: list = get_session_value(request, "stored_post_ids") or []

        post_id = int(request.POST['post_id']) 
        post_slug = request.POST['post_slug']     
        
        if post_id not in stored_post_ids:
            stored_post_ids.append(post_id)
        elif post_id in stored_post_ids:
            stored_post_ids.remove(post_id)
        
        request.session['stored_post_ids'] = stored_post_ids

        return HttpResponseRedirect(reverse("post-detail-page", args=[post_slug]))