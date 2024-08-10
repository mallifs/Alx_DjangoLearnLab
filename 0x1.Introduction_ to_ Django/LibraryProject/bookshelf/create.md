# Create Operation

## Python Command
```python
from your_app.models import Book
book = Book.objects.create(title="1984", author= “George Orwell”, publication_year=1949)
print(book)

##output
    ## !984 by George Orwell (1949)

    