from django.contrib import admin
from books.models import Book, Genre
from authors.models import Author


# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)