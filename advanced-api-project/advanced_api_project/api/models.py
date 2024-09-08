from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title





"""
Author Model:
    - name: stores the author's name.
    - Relationship: An author can have multiple books (one-to-many relationship).

Book Model:
    - title: stores the book's title.
    - publication_year: stores the year the book was published.
    - author: Foreign key to the Author model (Many-to-One relationship).
"""