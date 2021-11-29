from django.core.management import BaseCommand
import logging
from eclinic_platform.models import Categories

from eclinic_platform.tests.tests_category import get_categories

CATEGORIES = get_categories()

class Command(BaseCommand):

    help = "Create categories"

    def handle(self, *args, **options):
        for item in CATEGORIES:
            Categories.objects.create(
                            id=item["id"],
                            title=item["title"], 
                            sector=item["sector"],
                            image=item["image"],
                        )
            
        