from django.db import models
from django_countries.fields import CountryField

from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users")


DATA_TYPES = [
    ('Home', 'Home'),
    ('Accodmy', 'Accodmy'),
    ('Work', 'Work'),
    ('Other', 'Other')
]


class userPhoneNumber(models.Model):
    user = models.ForeignKey(
        User, related_name='user_phone', on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    type = models.CharField(choices=DATA_TYPES, max_length=10)


class UserAddrees (models.Model):
    user = models.ForeignKey(
        User, related_name='user_addrees', on_delete=models.CASCADE)
    type = models.CharField(choices=DATA_TYPES, max_length=10)
    country = CountryField()
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    streat = models.CharField(max_length=80)
    notes = models.CharField(max_length=150)
