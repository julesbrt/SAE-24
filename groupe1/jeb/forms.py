from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CapteurForm(ModelForm):
    class Meta:
        model = models.sensors

        fields = ('id','macaddr', 'piece', 'emplacement', 'nom')
        labels = {
            'macaddr': _('Numéro  '),
            'piece': _('Pièce '),
            'emplacement': _('Emplacement '),
            'nom': _('Nom '),
        }

class DonneeForm(ModelForm):
    class Meta:
        model = models.sensors_data

        fields = ('id','sensor_id', 'datetime', 'temp')
        labels = {
            'sensor_id': _('Numéro '),
            'datetime': _('Date & heure '),
            'temp': _('Temperature '),
        }
