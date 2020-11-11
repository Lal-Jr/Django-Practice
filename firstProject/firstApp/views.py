from django.shortcuts import render
from django.http import HttpResponse    

def index(request):
    myDict = {'insert_me':'HARISH'}
    return render(request,'firstApp/index.html',context=myDict)
