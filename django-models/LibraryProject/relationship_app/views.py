from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect


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

def register(request):
    return render(request, 'register.html')

def usercreationform_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    

def check_role(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(decorator)

@login_required
@check_role('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@check_role('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@check_role('Member')
def member_view(request):
    return render(request, 'member_view.html')
