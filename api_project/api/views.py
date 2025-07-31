from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view to list all Book instances.
    Uses BookSerializer to serialize the data.
    """
    queryset = Book.objects.all() # Defines the set of objects to retrieve
    serializer_class = BookSerializer # Specifies the serializer to use
