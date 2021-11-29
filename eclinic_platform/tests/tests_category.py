from django.test import TestCase

from eclinic_platform.models import Categories

categories = [
    {
        "image": "https://images.pexels.com/photos/6320167/pexels-photo-6320167.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Cardiology",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 1
    },
    {
        "image": "https://images.pexels.com/photos/4841224/pexels-photo-4841224.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Dermatology",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 2
    },
    {
        "image": "https://images.pexels.com/photos/4609046/pexels-photo-4609046.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Family Medicine",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 3
    },
    {
        "image": "https://images.pexels.com/photos/2014883/pexels-photo-2014883.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Obstetrics",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 4
    },
    {
        "image": "https://images.pexels.com/photos/9951388/pexels-photo-9951388.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Oncology",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 5
    },
    {
        "image": "https://images.pexels.com/photos/9951396/pexels-photo-9951396.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
        "title": "Orthopedic Surgery",
        "sector": "specialty",
        "doctors": 0,
        "hospitals": 0,
        "id": 6
    },
    {
        "image": "https://images.pexels.com/photos/3925819/pexels-photo-3925819.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Breast Cancer",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 7
    },
    {
        "image": "https://images.pexels.com/photos/8436729/pexels-photo-8436729.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
        "title": "Dementia",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 8
    },
    {
        "image": "https://images.pexels.com/photos/5690228/pexels-photo-5690228.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Endometriosis",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 9
    },
    {
        "image": "https://images.pexels.com/photos/9951405/pexels-photo-9951405.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Multiple Sclerosis",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 10
    },
    {
        "image": "https://images.pexels.com/photos/10046279/pexels-photo-10046279.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
        "title": "Fibromyalgia",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 11
    },
    {
        "image": "https://images.pexels.com/photos/6228273/pexels-photo-6228273.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
        "title": "Parkinson's Disease",
        "sector": "condition",
        "doctors": 0,
        "hospitals": 0,
        "id": 12
    },
    {
        "image": "https://images.pexels.com/photos/9951390/pexels-photo-9951390.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "ACL Surgery",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 13
    },
    {
        "image": "https://images.pexels.com/photos/9951386/pexels-photo-9951386.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "EEG (Electroencephalogram)",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 14
    },
    {
        "image": "https://images.pexels.com/photos/1030870/pexels-photo-1030870.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Hysterectomy",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 15
    },
    {
        "image": "https://images.pexels.com/photos/9889212/pexels-photo-9889212.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Knee Replacement",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 16
    },
    {
        "image": "https://images.pexels.com/photos/3733929/pexels-photo-3733929.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
        "title": "Multiple Sclerosis Therapy",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 17
    },
    {
        "image": "https://images.pexels.com/photos/1220757/pexels-photo-1220757.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "title": "Prostate Removal",
        "sector": "procedure",
        "doctors": 0,
        "hospitals": 0,
        "id": 18
    },
]

def get_categories():
    return categories

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        for item in categories:
            Categories.objects.create(title=item["title"], sector=item["sector"])
            