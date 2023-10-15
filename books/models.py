from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    poster = models.ImageField(upload_to='books/posters/', null=True, blank=True, verbose_name='Постер')
    description = models.TextField(verbose_name='Опис', null=True)
    publication_date = models.DateField(verbose_name='Дата пубікації')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)
    is_available = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'{self.title}/{self.author.first_name}{self.author.last_name}'

    class Meta:
        verbose_name = 'Книжка'
        verbose_name_plural = 'Книжки'
        ordering = ['title']


class Genre(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Жанр')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'
