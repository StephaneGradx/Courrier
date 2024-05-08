from django.db import models


# Create your models here.


class Courrier(models.Model):
    nomEmetteur = models.CharField(max_length=128)
    nomDestinataire = models.CharField(max_length=128)
    sujet = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    fichier = models.FileField()
    date = models.DateField()
    urgence = models.CharField(max_length=128)
    categorie = models.CharField(max_length=128)

class Rappel(models.Model):
    courrier = models.ForeignKey(Courrier, on_delete=models.CASCADE)
    date_rappel = models.DateField()
    description = models.CharField(max_length=255)