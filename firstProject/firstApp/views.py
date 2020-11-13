from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,AccessRecords,Webpage    

def index(request):
    webpages_list = AccessRecords.objects.order_by('date')
    date_dict = {'accessrecords':webpages_list}
    myDict = {'insert_me':'HARISH'}
    return render(request,'firstApp/index.html',context=date_dict)
