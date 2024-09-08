from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .views import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create a test book
        self.book = Book.objects.create(title="Test Book", author="John Doe", publication_year=2021)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'Imagine',
            'author': 'Bill Stones',
            'publication_year': 2020
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return one book

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Updated Book',
            'author': 'John Updated',
            'publication_year': 2022
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

def test_filter_books_by_author(self):
    url = f'/api/books/?author={self.book.author}'
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['author'], 'John Doe')

def test_search_books_by_title(self):
    url = f'/api/books/?search=Test Book'
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Test Book')

def test_order_books_by_publication_year(self):
    url = '/api/books/?ordering=-publication_year'
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['publication_year'], 2021)

def test_unauthorized_create_book(self):
    self.client.logout()  # Log out the user
    url = reverse('book-list')
    data = {
        'title': 'Unauthorized Book',
        'author': 'Unauthorized User',
        'publication_year': 2021
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)