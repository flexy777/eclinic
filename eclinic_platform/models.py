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
    image = models.ImageField(null=True, upload_to='categories', max_length=1024)
    keywords = models.TextField(max_length=5120, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Communication(models.Model):
   

    phone_enabled = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=50, null=True)

    whatsapp_enabled = models.BooleanField(default=True)
    whatsapp_number = models.CharField(max_length=50, null=True)

    zoom_enabled = models.BooleanField(default=True)
    zoom_link = models.CharField(max_length=255, null=True)

    google_meet_enabled = models.BooleanField(default=True)
    google_meet_link = models.CharField(max_length=255, null=True)

    email_enabled = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=250, null=True)


class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


USER_GROUPS =(
    ("SPECIALIST", "SPECIALIST"),
    ("USER", "USER"),
    ("ADMINISTRATOR", "ADMINISTRATOR")
)

GENDERS =(
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)

class User(AbstractUser):
    header_title = models.CharField(max_length=255)
    title = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
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
    avg_rating = models.FloatField(default=1.0)
    checkup_someone = models.BooleanField(default=False)
    online_consult = models.BooleanField(default=True)
    home_service = models.BooleanField(default=False)
    role = models.CharField(max_length=255, choices=USER_GROUPS, default="SPECIALIST")
    gender = models.CharField(max_length=20, choices=GENDERS, default="FEMALE")
    free_consultation = models.BooleanField(default=False)
    consultation_fee = models.FloatField(null = True)
    consultation_fee_duration = models.FloatField(null = True)
    communication_mode = models.OneToOneField(Communication, on_delete=models.CASCADE, null=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=5120)
    image = models.ImageField(null = True, upload_to='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

class Review(models.Model):
    comment = models.TextField(max_length=5120)
    rating = models.FloatField(default=1.0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

