from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.PositiveIntegerField(max_length=13, blank=True, null=True)
#

class Artifact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_posted =  models.DateTimeField(auto_now_add=True, null=True)
    is_sold = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
