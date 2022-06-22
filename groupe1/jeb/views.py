from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    data = list(models.sensors.objects.all())
    count = len(data)
    return render(request, 'index.html',{'data':data,'count':count})

def home(request):
    data1 = list(models.sensors_data.objects.all())
    count1 = len(data1)
    return render(request, 'index.html', {'data1': data1, 'count1': count1})