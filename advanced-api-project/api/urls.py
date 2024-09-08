# from django.contrib.auth import urls
from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView


urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name= 'books-detail'),
    path('books/create/', BookCreateView.as_view(), name = 'books-create'),
    path('books/list/', BookListView.as_view(), name = 'books-list'),
    path('books/update/', BookUpdateView.as_view(), name = 'books-update'),
    path('books/delete/', BookDeleteView.as_view(), name = 'books-delete'),


]