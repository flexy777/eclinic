from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

from eclinic_platform.utilities.methods import toFileUrl


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
    is_verified = models.BooleanField(default=False)

    def get_favourites(self):
        favs = Favourite.objects.filter(user_id = self.pk).values_list('specialist_id', flat=True)    
        return User.objects.filter(pk__in = favs)

    def get_related_specialists(self):
        return User.objects.exclude(pk = self.pk)[:10]
    
    def get_name(self):
        return self.first_name+" "+self.last_name

    def my_appointments(self):
        return Appointment.objects.filter(Q(patient=self)|Q(specialist=self))

    def get_image(self):
        return toFileUrl(self.image)



class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=5120)
    image = models.ImageField(null = True, upload_to='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

RATINGS =[
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1)
]

class Review(models.Model):
    comment = models.TextField(max_length=5120)
    rating = models.IntegerField(default=1.0, choices=RATINGS)
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


class Communication(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=1)
    
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



class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_user')
    specialist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_specialist')

TRANSACTION_TYPE =(
    ("DEBIT", "DEBIT"),
    ("CREDIT", "CREDIT")
)

TRANSACTION_STATUS =(
    ("PENDING", "PENDING"),
    ("SUCCESS", "SUCCESS"),
    ("FAILED", "FAILED")
)
PAYMENT_MODE =(
    ("PAYSTACK", "PAYSTACK"),
    ("FLUTTERWAVE", "FLUTTERWAVE"),
    ("PAYPAL", "PAYPAL")
)

class Transactions(models.Model):
    amount = models.FloatField(null=True)
    type = models.CharField(max_length=255, choices=TRANSACTION_TYPE)
    status = models.CharField(max_length=255, choices=TRANSACTION_STATUS)
    note = models.TextField(max_length=5120)
    payment_mode = models.CharField(max_length=255, choices=PAYMENT_MODE, default="PAYSTACK")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', null=True)


    
APPOINTMENT_STATUS =(
    ("PENDING", "PENDING"),
    ("ACCEPTED", "ACCEPTED"),
    ("DECLINED", "DECLINED"),
    ("COMPLETED", "COMPLETED")
)

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    specialist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='specialist')
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS, default="PENDING")
    date_time = models.DateTimeField()
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=5120)

class AppointmentDetails(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=5120)
    score = models.IntegerField(null=True)
    recommendations = models.TextField(max_length=5120)

