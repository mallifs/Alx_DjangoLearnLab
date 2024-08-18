import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(f'Book Title: {book.title}')
    except Author.DoesNotExist:
        print('Author not found')

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f'Book Title: {book.title}')
    except Library.DoesNotExist:
        print('Library not found')

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f'Librarian Name: {librarian.name}')
    except Library.DoesNotExist:
        print('Library not found')
    except Librarian.DoesNotExist:
        print('Librarian not found')

if __name__ == '__main__':
    query_all_books_by_author('Author Name')
    list_all_books_in_library('Library Name')
    retrieve_librarian_for_library('Library Name')
