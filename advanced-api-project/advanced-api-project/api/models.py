from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
from django.db import models


class Author(models.Model):
    """
    The Author model stores the name of the author.
    One author can write many books, hence the one-to-many relationship
    with the Book model.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model stores information about a book.
    Each book has a title, publication year, and is linked to an Author
    through a foreign key relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
