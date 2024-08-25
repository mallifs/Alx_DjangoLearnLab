# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]
