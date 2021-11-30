from django.core.management import BaseCommand
import logging
from eclinic_platform.models import Categories, Review, User
from faker import Faker
from random import randrange
import numpy as np  
fake = Faker()


class Command(BaseCommand):

    help = "Create categories"

    def handle(self, *args, **options):
        for item in range(randrange(53)):
            
            try:
                user = {
                    "comment": fake.text(),
                    "rating": [1,2,3,4,5][randrange(5)],
                    "customer_id": [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20][randrange(20)],
                    "doctor_id": 1
                }
                
                _user = Review(**user)
                _user.save()
                
            except Exception as e:
                print(e)       
        