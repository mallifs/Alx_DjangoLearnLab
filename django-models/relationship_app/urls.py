from django.urls import path
from .views import book_list, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]