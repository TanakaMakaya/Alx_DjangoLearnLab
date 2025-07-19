>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> all_books = Book.objects.all()
>>> print(f"Remaining books: {all_books}")
Remaining books: <QuerySet []>
>>> print(f"Book count: {Book.objects.count()}")
Book count: 0
>>> try:
...     deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
...     print("Book still exists")
... except Book.DoesNotExist:
...     print("Book successfully deleted - does not exist")
... 
Book successfully deleted - does not exist