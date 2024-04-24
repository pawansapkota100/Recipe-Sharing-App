from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic= models.ImageField(upload_to='profile_pic',blank=True)
    bio= models.CharField(max_length=100, null=True, blank=True)
    age= models.CharField(max_length=100, null=True, blank=True)
    address= models.CharField(max_length=100, null=True, blank=True)
    phone= models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.user.username