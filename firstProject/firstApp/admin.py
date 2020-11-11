from django.contrib import admin
from firstApp.models import Webpage, Topic, AccessRecord
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
