from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based
    path('logout/', views.logout_view, name='logout'),  # Function-based
    path('register/', views.register_view, name='register'),  # Function-based
    path('login/', views.LogintView.as_view(template_name='login.html'), name='login'),  # Class-based
]
