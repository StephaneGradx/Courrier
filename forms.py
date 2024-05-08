from django import forms

from Dashboard.models import Rappel


class CourrierForm(forms.Form):
    nomEmetteur = forms.CharField(label="Expediteur", max_length=128)
    nomDestinataire = forms.CharField(label="Destinataire", max_length=128)
    sujet = forms.CharField(label="Sujet", max_length=128)
    Description = forms.CharField(label="Description", widget=forms.Textarea())
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type': 'date'}))
    CATEGORIES = [("appel d'offre","Appel d'offre"), 
                  ("pipeline","Pipeline"), 
                  ("reunion de synthese","Reunion de synthese"),
                  ("autre", "Autre")]
    categorie = forms.ChoiceField(label="Categorie", choices=CATEGORIES)
    URGENCES = [("haute", "Haute"),
                ("moyenne", "Moyenne"),
                ("basse", "Basse")]
    urgence = forms.ChoiceField(label="Urgence", choices=URGENCES)
    fichier = forms.FileField(label="Courrier")

class RappelForm(forms.ModelForm):
     date_rappel = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
     description = forms.CharField(max_length=255, widget=forms.Textarea())

     class Meta:
        model = Rappel
        fields = ['date_rappel', 'description']