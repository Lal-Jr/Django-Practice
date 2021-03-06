import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')

import django
django.setup()

import random
from faker import Faker
try: 
    fakegen = Faker()
    topics =['Search','Social','Marketplace','News','Games']

    def addTopic():
        t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
        t.save()
        return t

    def populate(N=5):
        for entry in range(N):
            # get the topic for the entry
            top = addTopic()

            # create the fake data for the entry
            fake_url = fakegen.url()
            fake_name = fakegen.company()

            #create new webpage entry
            webpge =  Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

    if __name__ == "__main__":
        print("populating script")
        populate(20)
        print("populating complete")

except:
    AttributeError
    print("Error Occuring")