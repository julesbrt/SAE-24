from django.forms import model_to_dict
from django.shortcuts import render

from groupe1.jeb.models import Capteur

def info(request):
    return render(request, 'capteur/info.html')

def update(request):
    capteur = models.Capteur.objects.get(pk=id)
    form = CapteurForm(model_to_dict(capteur))
    return render(request, 'capteur/update.html', {'id': id, 'form': form})

def affiche(request):
    capteur = models.Capteur.objects.all()
    return render(request, 'capteur/affiche.html', {'capteur': capteur})