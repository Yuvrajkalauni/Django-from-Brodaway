from django.core.management.base import BaseCommand
from meals.models import Meal_Plan
import random
from django.contrib.auth.models import User
from faker import Faker #for generating fake date (uv add faker)

class Command(BaseCommand):
    help = "Add meal plan"

    fake = Faker()   #create object

    def handle(self, *args, **options):
        user = User.objects.all().values_list('id')
        n = 340
        for i in range(1,n):
            Meal_Plan.objects.create(
                user_id = random.choice(user)[0],
                start_date = self.fake.date_between(start_date='-10y'),
                end_date = self.fake.date_between(start_date='-4y', end_date='today')
            )
            self.stdout.write(self.style.SUCCESS(f'{i}/{n-1} number completed'))
            