from django.db import models


class PasswordEntry(models.Model):
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
