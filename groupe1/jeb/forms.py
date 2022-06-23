from . import models
from django.forms import ModelForm

class SensorsForm(ModelForm):
    class Meta:
        model = models.sensors1
        fields = ('emplacement', 'nom')
        labels = {
            'nom': 'Nom',
            'emplacement': 'Emplacement'
        }