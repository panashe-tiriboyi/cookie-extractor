from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    STATUS = (
        ('regular','regular'),
        ('staff','staff'),
        ('moderator','moderator')
    )
    email = models.EmailField(max_length=254, unique=True, db_index=True, primary_key=True)
    status = models.CharField(max_length=100, choices= STATUS, default='regular')
    description = models.TextField('Descrtiption', max_length=600, default='', blank=True)

    def __str__(self):
        return self.username
