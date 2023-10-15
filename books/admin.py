from django.contrib import admin

from books.models import Book, Genre

admin.site.register(Book)
admin.site.register(Genre)
