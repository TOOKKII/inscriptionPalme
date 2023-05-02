from django.db import models
from PIL import Image
from django_cryptography.fields import encrypt

# Create your models here.

class Inscription(models.Model):
    nom = encrypt(models.CharField(max_length=50))
    prenom = encrypt(models.CharField(max_length=50))
    date_naissance = encrypt(models.DateTimeField(max_length=50))
    mail = encrypt(models.CharField(max_length=50))
    telephone = encrypt(models.CharField(max_length=20))
    adresse = encrypt(models.CharField(max_length=50))
    code_postal = encrypt(models.CharField(max_length=5))
    date_inscription = encrypt(models.DateTimeField(max_length=50))
    fiche_inscription = encrypt(models.ImageField(null=True))#(upload_to='tkt'))
    certificat_medical = encrypt(models.ImageField(null=True))#(upload_to='tkt2'))
    date_certificat = encrypt(models.DateTimeField(max_length=50, null=True))
    autorisation_parentale = encrypt(models.ImageField(null=True))#(upload_to='tkt3'))
    photo = encrypt(models.ImageField(null=True))#(upload_to='tkt4'))
    
    #ficheInscr = Image.open("tkt")
    #certifMédi = Image.open("tkt2")
    #autoParen = Image.open("tkt3")
    #photo = Image.open("tkt4")

    def __str__(self):
            return self.nom


class Adherents(models.Model):
    idInscription= models.ForeignKey(Inscription,on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(max_length=50)
    mail = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    code_postal = models.IntegerField()
    membre = models.CharField(max_length=50)

    def __str__(self):
        return self.idInscription

class Categorie(models.Model):
    idAdherent= models.ForeignKey(Adherents,on_delete=models.CASCADE)
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

class Statut(models.Model):
    idAdherent= models.ManyToManyField(Adherents)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return self.statut