from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    #example of custom fields
    age = models.IntegerField()
    profile_pic = models.ImageField(blank=True)

    #USERNAME_FIELD = 'field which have unique equal to True default is username'
    REQUIRED_FIELDS = ['email', 'age', 'profile_pic']

    def __str__(self):
        return self.email
