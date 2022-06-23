from django.shortcuts import render, HttpResponseRedirect
from .models import sensors1, sensors_data
from .forms import SensorsForm


def index(request):
    return render(request, 'index.html')

def capteur(request):
    sensors = sensors1.objects.all()
    return render(request, 'capteur/info.html', {'sensors': sensors})

def donnee(request):
    data = sensors_data.objects.all()
    return render(request, 'donnee/info.html', {'data': data})

def update(request, id):
    sensors = sensors1.objects.get(pk=id)
    form = SensorsForm(sensors1.dico())
    return render(request, "capteur/info.html",{"form":form, "id":id})

def updatetraitement(request, id):
    form = SensorsForm(request.POST)
    if form.is_valid():
        sensors = form.save(commit=False)
        sensors.id = id
        sensors.save()
        return HttpResponseRedirect("/info.html")
    else:
        return render(request, "capteur/update.html", {"form": form, "id":id})


"""
def delete(request, id):
    client = models.client.objects.get(pk=id)
    commande = models.commande.objects.filter(client_id = id)
    client.delete()
    commande.delete()
    return HttpResponseRedirect("/infos_client/")
"""