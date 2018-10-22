from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.urlresolvers import reverse

# # Create your models here.
#
# class Location(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#
# class Neighbourhood(models.Model):
#     neighbourhood_photo = models.ImageField(upload_to='neighbourhood/')
#     neighbourhood_name = models.CharField(max_length=100, blank=True, null=True)
#     occupants_count = models.IntegerField(blank=True, null=True)
#     neighbourhood_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
#     admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#
#
# class Business(models.Model):
#     business_photo = models.ImageField(upload_to='business/')
#     business_name = models.CharField(max_length=100, blank=True, null=True)
#     business_description = models.TextField(max_length=200, blank=True, null=True)
#     business_email = models.CharField(max_length=100, blank=True, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    profile_photo = ImageField(upload_to='profile/')
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField(max_length=140, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
