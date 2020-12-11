from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    
    
    dests=Destination.objects.all()
    return render(request,"index.html",{"dests":dests})

def about(request):
    return render(request,'about.html')


def contant(request):
    return render(request,'contant.html')

def service(request):
    return render(request,'service.html')
