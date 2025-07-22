

from django.contrib import admin
from .models import Book
from .models import CustomUser, CustomUserAdmin

# Basic registration (simple approach)
# admin.site.register(Book)

# Advanced registration with customization (recommended approach)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for these fields
    search_fields = ('title', 'author')
    
    # Add filter sidebar for these fields
    list_filter = ('publication_year', 'author')
    
    # Set default ordering
    ordering = ('title',)
    
    # Number of items per page
    list_per_page = 25
    
    # Make fields clickable in list view (links to edit page)
    list_display_links = ('title',)
    
    # Optional: Customize the form layout in add/edit view
    fields = ('title', 'author', 'publication_year')
    
    # Optional: Add fieldsets for better organization (alternative to fields)
    # fieldsets = (
    #     ('Book Information', {
    #         'fields': ('title', 'author', 'publication_year')
    #     }),
    # )

admin.site.register(CustomUser, CustomUserAdmin)