from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=100,default="")
    phone=models.IntegerField(default=0)
    city=models.CharField(max_length=20,default="")
    website=models.URLField(default="")

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)

