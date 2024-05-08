from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Dashboard.forms import CourrierForm, RappelForm
from Dashboard.models import Courrier, Rappel

# Create your views here.

def index(request):
    courrier = Courrier.objects.first()  # Choisissez un courrier à afficher
    rappels = Rappel.objects.all()  # Supposons que vous récupérez tous les rappels
    return render(request, 'index.html', {'courrier': courrier, 'rappels': rappels})

@login_required
def courrier(request):
    if request.method == "POST":
        form = CourrierForm(request.POST, request.FILES)
        if form.is_valid():
            courrier = Courrier(
                nomEmetteur=form.cleaned_data['nomEmetteur'],
                nomDestinataire=form.cleaned_data['nomDestinataire'],
                sujet=form.cleaned_data['sujet'],
                description=form.cleaned_data['Description'],
                date=form.cleaned_data['date'],
                categorie=form.cleaned_data['categorie'],
                urgence = form.cleaned_data['urgence'],
                fichier=form.cleaned_data['fichier']  
            )
            courrier.save()
            return redirect('index')
    else:
        form = CourrierForm()

    return render(request, "courrier.html", {"form": form})

def rappel(request):
    if request.method == "POST":
        form = RappelForm(request.POST)
        if form.is_valid():
            rappel = Rappel(
                date_rappel=form.cleaned_data['date_rappel'],
                description=form.cleaned_data['description']
            )
            rappel.save()
            return HttpResponse("Le formulaire a été soumis avec succès. Données enregistrées.")
    else:
        form = RappelForm()

    return render(request, "rappel.html", {"form": form})
@login_required
def details_courrier(request, courrier_id):
    courriers = Courrier.objects.all()
    return render(request, 'details_courrier.html', {'courriers': courriers})

def create_rappel(request, courrier_id):
    if request.method == "POST":
        form = RappelForm(request.POST)
        if form.is_valid():
            courrier = Courrier.objects.get(id=courrier_id)
            date_rappel = form.cleaned_data['date_rappel']
            description = form.cleaned_data['description']
            # Créez un nouvel objet Rappel avec les données du formulaire
            Rappel.objects.create(courrier=courrier, date_rappel=date_rappel, description=description)
            return redirect('index')  # Redirigez vers la liste des rappels après la création
    else:
        form = RappelForm()
    return render(request, "create_rappel.html", {"form": form})

def update_rappel(request, rappel_id):
    rappel = Rappel.objects.get(id=rappel_id)
    if request.method == "POST":
        form = RappelForm(request.POST, instance=rappel)
        if form.is_valid():
            form.save()  # Enregistrez directement le formulaire si valide
            return redirect('index')  # Redirigez vers la liste des rappels après la mise à jour
    else:
        form = RappelForm(instance=rappel)
    return render(request, "update_rappel.html", {"form": form})

def delete_rappel(request, rappel_id):
    rappel = Rappel.objects.get(id=rappel_id)
    rappel.delete()
    return redirect('index') 