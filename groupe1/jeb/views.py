from django.shortcuts import render
from .models import sensors1, sensors_data
from .forms import SensorsForm
from django.http import HttpResponseRedirect , HttpResponse
from django.forms.models import model_to_dict
import csv


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
    form = SensorsForm(model_to_dict(sensors))
    if request.method == "POST":
        form = SensorsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/capteur/info")
    else:
        return render(request, "capteur/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    sensors = SensorsForm(request.POST)
    bak = sensors1.objects.get(id=id)
    if sensors.is_valid():
        sensors = sensors.save(commit=False)
        sensors.id = id
        sensors.macaddr = bak.macaddr
        sensors.piece = bak.piece
        sensors.save()
        return HttpResponseRedirect("/capteur/info.html")
    else:
        return render(request, "capteur/info.html", {"form": sensors, "id": id})

def export_csv(request, id):
    data = sensors_data.objects.filter(sensor = id)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="export.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['timestamp', 'macaddr', 'piece', 'emplacement', 'nom', 'temp'])
    for i in data:
        writer.writerow(
            [i.datetime,
            i.sensor.macaddr,
            i.sensor.piece,
            i.sensor.emplacement,
            i.sensor.nom,
            i.temp])

    return response

"""
def delete(request, id):
    client = models.client.objects.get(pk=id)
    commande = models.commande.objects.filter(client_id = id)
    client.delete()
    commande.delete()
    return HttpResponseRedirect("/infos_client/")
"""