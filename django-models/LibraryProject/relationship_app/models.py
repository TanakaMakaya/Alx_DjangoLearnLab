from django.db import models

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(author, on_delete=models.CASCADE)

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(library, on_delete=models.CASCADE)