from django.core.management import BaseCommand
import logging
from eclinic_platform.models import Categories, User
from faker import Faker
from random import randrange
import numpy as np  
fake = Faker()


class Command(BaseCommand):

    help = "Create categories"

    def handle(self, *args, **options):
        for item in range(randrange(1000)):
            
            try:
                profile = fake.simple_profile()
                first_name = profile["name"].split(" ")[0]
                last_name = profile["name"].split(" ")[1]
                email = fake.free_email()
                username = (last_name+"_"+first_name+"_"+str(randrange(1000))).lower()
                
                user = {
                    "password": "123456",
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "gender": "MALE" if (profile["sex"] is "M") else "FEMALE",
                    "phone": fake.phone_number(),
                    "header_title": fake.sentence(),
                    "title": ["Dr", "Nurse", "Surgeon", "Dentist"][randrange(4)],
                    "background_image": None,
                    "image": None,
                    "about": fake.text(),
                    "location_address": ["Abuja", "Lagos", "Ibadan", "Lagos", "Abuja", "Kaduna", "Kano", "Port Harcour", "Owerri", "Benin City", "Minna"][randrange(11)],
                    "location_lat": None,
                    "location_lng": None,
                    "avg_rating": randrange(5),
                    "checkup_someone": [False, True][randrange(2)],
                    "online_consult": [False, True][randrange(2)],
                    "home_service": [False, True][randrange(2)],
                    "role": "SPECIALIST"
                }
                _user = User(**user)
                _user.save()
                
                ids = np.random.randint(18, size=(4))
                for i in ids:
                    if(i.item() > 0):
                        _user.category.add(Categories.objects.get(pk=i.item()))
            except:
                continue        
        