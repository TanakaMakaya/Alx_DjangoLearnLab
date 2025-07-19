from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView
from django.http import HttpResponse

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'list_books.html'
    context_object_name = 'library'