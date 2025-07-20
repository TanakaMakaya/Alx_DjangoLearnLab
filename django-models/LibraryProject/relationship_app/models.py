from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

class UserProfile(models.Mode):
    admin = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    member = models.ForeignKey(Library, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
