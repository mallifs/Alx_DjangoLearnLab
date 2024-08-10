# Delete Operation

## Python Command
```python
from bookshelf.models import Book
retrieved_book.delete()

try:
    Book.objects.get(title="My Updated Book")
except Book.DoesNotExist:
    print("Book successfully deleted.")

##Output
    ## Book successfully deleted.