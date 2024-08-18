from django.urls import path
from .views import book_list, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import RegisterView
from django.contrib import admin
from .views import admin_view
from .views import librarian_view
from .views import member_view

 

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]