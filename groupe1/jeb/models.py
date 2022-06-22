# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
    #   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class sensors(models.Model):
    id = models.AutoField(primary_key=True)
    macaddr = models.CharField(max_length=45, blank=True)
    piece = models.CharField(max_length=45)
    emplacement = models.CharField(max_length=45, blank=True, null=True)
    nom = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensors'


class sensors_data(models.Model):
    id = models.AutoField(primary_key=True)
    sensors_id = models.OneToOneField(sensors, models.DO_NOTHING, db_column='macaddr')
    datetime = models.DateTimeField(unique=True)
    temp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensors_data'
