from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from eclinic_platform.models import Review
from django.db.models import Avg

def update_review(instance):
    rating = Review.objects.filter(doctor=instance.doctor).aggregate(Avg('rating'))
    instance.doctor.avg_rating = round(rating["rating__avg"], 2)
    instance.doctor.save()

@receiver(post_save, sender=Review) 
def update_rating(sender, instance, created, **kwargs):
    update_review(instance) 

@receiver(post_delete, sender=Review) 
def update_rating(sender, instance, created, **kwargs):
    update_review(instance)