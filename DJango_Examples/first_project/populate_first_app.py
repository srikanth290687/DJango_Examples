import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Create Fake Population script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ["Social", "News", "Search", "Marketplace"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Add some topic
        top = add_topic()
        # Create a fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        accrec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script(s)")
    populate(20)
    print("Populating Script(s) Completed")
