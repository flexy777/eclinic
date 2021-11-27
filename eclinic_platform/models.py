from django.db import models

# Create your models here.
SECTORS =(
    ("SPECIALITY", "SPECIALITY"),
    ("CONDITION", "CONDITION"),
    ("PROCEDURE", "PROCEDURE")
)
class Categories(models.Model):
    title = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, choices=SECTORS)
    image = models.ImageField(null=True)
    keywords = models.TextField(max_length=5120, null=True)

