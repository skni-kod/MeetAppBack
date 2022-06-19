from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator
import uuid
# Create your models here.


class Event(models.Model):
    Event_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(null=True,blank=True)
    x = models.FloatField(null=False,blank=False,default=0)
    y = models.FloatField(null=False,blank=False,default=0)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(blank=True,null=True,upload_to='profiles/', default="profiles/default.jpeg")
    created = models.DateTimeField(auto_now_add=True)
    Profile_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Profile_Event_Relation(models.Model):
    Profile_ID = models.ForeignKey(Profile,on_delete =models.CASCADE)
    Event_ID = models.ForeignKey(Event,on_delete =models.CASCADE)
    Owner =  models.BooleanField(default=False)
