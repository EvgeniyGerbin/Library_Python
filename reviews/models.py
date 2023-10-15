from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from mylibrary import settings
class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} rating: {self.rating}'