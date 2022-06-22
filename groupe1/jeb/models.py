# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
    #   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Capteur(models.Model):
    numero = models.AutoField(primary_key=True)
    piece = models.CharField(max_length=45)
    emplacement = models.CharField(max_length=45, blank=True, null=True)
    nom = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capteur'


class Donnee(models.Model):
    numero = models.OneToOneField(Capteur, models.DO_NOTHING, db_column='numero', primary_key=True)
    timestomp = models.DateTimeField(unique=True)
    temperature = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donnee'
