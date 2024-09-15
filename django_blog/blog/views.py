from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # This will be created later

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    return render(request, 'blog/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import CommentForm

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, post=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm(post=post)
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('post-detail', pk=self.object.post.pk)

@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/edit_comment.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '/'
    template_name = 'blog/delete_comment.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})