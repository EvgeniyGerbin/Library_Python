from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # додаткові поля тут
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
