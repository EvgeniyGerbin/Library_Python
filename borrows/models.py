from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from mylibrary import settings

class Borrow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.book} - {self.borrow_date}"
