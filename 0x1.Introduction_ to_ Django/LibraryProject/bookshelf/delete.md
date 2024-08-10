# Delete Operation

## Python Command
```python
retrieved_book.delete()

try:
    Book.objects.get(title="My Updated Book")
except Book.DoesNotExist:
    print("Book successfully deleted.")

##Output
    ## Book successfully deleted.
    