from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
  
   def __str__(self):
       return self.name

class User(models.Model):
   
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    dob = models.DateField()
    img = models.ImageField(upload_to="home/media/user.png",default= " ")

    def __str__(self):
        return self.name
    

   