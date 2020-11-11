import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')

import django
django.setup()

import random
from firstApp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
