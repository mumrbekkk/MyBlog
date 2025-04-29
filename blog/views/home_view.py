from django.views.generic import ListView
from ..models.post_model import Post


class HomeView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["title"]
    context_object_name = "posts"

    def get_queryset(self):
        data = super().get_queryset()
        data = data[:3]
        return data
