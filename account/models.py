from django.db import models
from django_countries.fields import CountryField
from utils.genrate_code import genrate_code
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
'''
DjangoUser:
        - user-name
        - first name
        - last name
        - password
        - email
'''

class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users")
    code = models.CharField(max_length=10, default=genrate_code)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_profile(sender, created, instance,**kwargs):
    if created :
        profile.objects.create(user=instance)

    
    



DATA_TYPES = [
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Other', 'Other'),
]


class userPhoneNumber(models.Model):
    user = models.ForeignKey(
        User, related_name='user_phone', on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    data_type = models.CharField(choices=DATA_TYPES, max_length=10)

    def __str__(self):
        return str(self.user)
    



class UserAddrees (models.Model):
    user = models.ForeignKey(
        User, related_name='user_addrees', on_delete=models.CASCADE)
    data_type = models.CharField(choices=DATA_TYPES, max_length=10)
    country = CountryField()
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    streat = models.CharField(max_length=80)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)