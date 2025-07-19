# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by checking all books
all_books = Book.objects.all()
print(f"Remaining books: {all_books}")
print(f"Book count: {Book.objects.count()}")