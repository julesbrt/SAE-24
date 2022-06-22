from django.forms import model_to_dict
from django.shortcuts import render
from . import models
from .forms import DonneeForm

from groupe1.jeb.models import Donnee

def info(request):
    return render(request, 'donnee/info.html')

def update(request):
    donnee = models.Donnee.objects.get(pk=id)
    form = DonneeForm(model_to_dict(donnee))
    return render(request, 'donnee/update.html', {'id': id, 'form': form})

def affiche(request):
    donnee = models.Donnee.objects.all()
    return render(request, 'donnee/affiche.html', {'donnee': donnee})