# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author():
    """
    Query all books by a specific author using ForeignKey relationship
    """
    print("=== Query: All books by a specific author ===")
    
    # Example 1: Get all books by a specific author name
    author_name = "J.K. Rowling"  # Replace with actual author name in your database
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    
    # Example 2: Using related_name (reverse relationship)
    try:
        author = Author.objects.get(name=author_name)
        books = author.book_set.all()  # Using reverse ForeignKey relationship
        
        print(f"\nUsing reverse relationship - Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    
    # Example 3: Get all authors and their books
    print("\nAll authors and their books:")
    authors = Author.objects.all()
    for author in authors:
        books = author.book_set.all()
        print(f"{author.name}:")
        for book in books:
            print(f"  - {book.title}")
        print()

def list_all_books_in_library():
    """
    List all books in a library using ManyToManyField relationship
    """
    print("=== Query: List all books in a library ===")
    
    # Example 1: Get all books in a specific library
    library_name = "Central Library"  # Replace with actual library name in your database
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    
    # Example 2: Get all libraries that have a specific book
    book_title = "Harry Potter and the Philosopher's Stone"  # Replace with actual book title
    try:
        book = Book.objects.get(title=book_title)
        libraries = book.library_set.all()  # Using reverse ManyToMany relationship
        
        print(f"\nLibraries that have '{book_title}':")
        for library in libraries:
            print(f"  - {library.name}")
    except Book.DoesNotExist:
        print(f"Book '{book_title}' not found.")
    
    # Example 3: Get all libraries and their books
    print("\nAll libraries and their books:")
    libraries = Library.objects.all()
    for library in libraries:
        books = library.books.all()
        print(f"{library.name}:")
        if books.exists():
            for book in books:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print("  - No books available")
        print()

def retrieve_librarian_for_library():
    Librarian.objects.get(library=library)
    """
    Retrieve the librarian for a library using OneToOneField relationship
    """
    print("=== Query: Retrieve librarian for a library ===")
    
    # Example 1: Get librarian for a specific library
    library_name = "Central Library"  # Replace with actual library name in your database
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using reverse OneToOne relationship
        
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
    
    # Example 2: Get library for a specific librarian
    librarian_name = "Alice Johnson"  # Replace with actual librarian name in your database
    try:
        librarian = Librarian.objects.get(name=librarian_name)
        library = librarian.library
        
        print(f"Library managed by {librarian_name}: {library.name}")
    except Librarian.DoesNotExist:
        print(f"Librarian '{librarian_name}' not found.")
    
    # Example 3: Get all librarians and their libraries
    print("\nAll librarians and their libraries:")
    librarians = Librarian.objects.all()
    for librarian in librarians:
        print(f"{librarian.name} manages {librarian.library.name}")
    
    # Example 4: Get all libraries and their librarians
    print("\nAll libraries and their librarians:")
    libraries = Library.objects.all()
    for library in libraries:
        try:
            librarian = library.librarian
            print(f"{library.name} - Librarian: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"{library.name} - No librarian assigned")

def create_sample_data():
    """
    Create sample data for testing the relationships
    """
    print("=== Creating sample data ===")
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Harper Lee")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    book5 = Book.objects.create(title="To Kill a Mockingbird", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!")

if __name__ == "__main__":
    # Uncomment the line below to create sample data first
    # create_sample_data()
    
    # Run the queries
    query_all_books_by_author()
    print("\n" + "="*50 + "\n")
    
    list_all_books_in_library()
    print("\n" + "="*50 + "\n")
    
    retrieve_librarian_for_library()