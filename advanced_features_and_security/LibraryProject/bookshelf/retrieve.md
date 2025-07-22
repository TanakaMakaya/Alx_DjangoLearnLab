# Retrieve the specific book
book = Book.objects.get(title="1984")

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")