from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
SECTORS =(
    ("SPECIALITY", "SPECIALITY"),
    ("CONDITION", "CONDITION"),
    ("PROCEDURE", "PROCEDURE")
)
class Categories(models.Model):
    title = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, choices=SECTORS)
    image = models.ImageField(null=True, upload_to='categories')
    keywords = models.TextField(max_length=5120, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class User(AbstractUser):
    header_title = models.CharField(max_length=255)
    title = models.CharField(max_length=50, null=True)
    background_image = models.ImageField(null=True, upload_to='usersBg')
    image = models.ImageField(null=True, upload_to='users')
    category = models.ManyToManyField(Categories)
    about = models.TextField(max_length=5120)
    location_address = models.CharField(max_length=255)
    location_lat = models.FloatField(null=True)
    location_lng = models.FloatField(null =True)
    location_address_component = models.TextField(max_length=5120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=5120)
    image = models.ImageField(null = True, upload_to='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   