from django.urls import path
from .views import home_view, posts_view, post_detail_view, read_later_view, login_view ,register_view, logout_view

urlpatterns = [
    path('', home_view.HomeView.as_view(), name='starting-page'),
    path('posts', posts_view.PostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', post_detail_view.PostDetailView.as_view(), name='post-detail-page'),
    path('stored-posts', read_later_view.ReadLaterView.as_view(), name="stored-posts-page"),
    # Test
    path('login', login_view.LoginFormView.as_view(), name='login-page'),
    path('register', register_view.RegisterFormView.as_view(), name='register-page'),
    path('logout', logout_view.logout_view, name='logout-page'),
]
