from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    poster = models.ImageField(upload_to='authors/posters/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
