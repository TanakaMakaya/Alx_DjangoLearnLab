from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Function-based view for listing books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def login_view(request):
    # Your login logic here
    return render(request, 'login.html')
def logout_view(request):
    # Your logout logic here
    return render(request, 'logout.html')
def register_view(request):
    # Your registration logic here
    return render(request, 'register.html')
