from django.db import models

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=1880)

    def __str__(self):
        return self.title

class Meta:
        permissions = [
            ("can_add_book", "add book"),
            ("can_change_book", "change book"),
            ("can_delete_book", "delete book"),
        ]    