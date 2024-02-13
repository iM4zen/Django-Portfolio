# in your_app/models.py

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    web_developer = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return self.name
