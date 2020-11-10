from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("MY PROJECT")

def help(request):
    myDict = { 'insertMe' : "HELP"}
    return render(request,'secondApp/index.html',context=myDict)
