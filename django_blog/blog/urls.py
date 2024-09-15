from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


from django.urls import path
from . import views

urlpatterns = [
    # ... existing URL patterns ...
    path('post/<int:post_id>/comments/', views.post_comments, name='post_comments'),
    path('post/<int:post_id>/comments/new/', views.create_comment, name='create_comment'),
    path('comment/<int:pk>/update/', views.update_comment, name='update_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/comments/new/', views.create_comment, name='create_comment'),
]



from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_posts  # Add import
)

urlpatterns = [
    # Existing URL patterns

    # URL pattern for searching posts
    path('search/', search_posts, name='search-posts'),

    # URL pattern for viewing posts by tag
    path('tags/<str:tag_name>/', PostListView.as_view(), name='posts-by-tag'),
    path("tags/<slug:tag_slug>/", "PostByTagListView.as_view()")
]