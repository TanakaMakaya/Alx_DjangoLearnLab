from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view to list all Book instances.
    Uses BookSerializer to serialize the data.
    """
    queryset = Book.objects.all() # Defines the set of objects to retrieve
    serializer_class = BookSerializer # Specifies the serializer to use

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Book model.
    """
    queryset = Book.objects.all() # Defines the set of objects to retrieve
    serializer_class = BookSerializer # Specifies the serializer to use