from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# --------------------
# LIST & CREATE VIEW
# --------------------
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles:
    - GET /books/ → list all books
    - POST /books/ → create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can POST (create)
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# --------------------
# RETRIEVE, UPDATE, DELETE VIEW
# --------------------
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles:
    - GET /books/<id>/ → retrieve book by ID
    - PUT/PATCH /books/<id>/ → update book
    - DELETE /books/<id>/ → delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Auth required for update & delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
