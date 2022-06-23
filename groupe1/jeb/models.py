from django.db import models


class sensors1(models.Model):
    macaddr = models.CharField(unique=True, max_length=12)
    piece = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensors'


class sensors_data(models.Model):
    sensor = models.ForeignKey(sensors1, models.DO_NOTHING)
    datetime = models.DateTimeField()
    temp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sensors_data'
