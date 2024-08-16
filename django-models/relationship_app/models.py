from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= "books")  

    def __str__(self):
        return self.title  


class Library(models.Model):
    name= models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name= "libraries")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name