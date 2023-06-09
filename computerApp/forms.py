from django import forms
from .models import Machine
from .models import Utilisateur
from .models import ContactMessage
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de la machine")
    ip = forms.CharField(required=True, label="IP de la machine")

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) >20 :
            raise ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_ip(self):
        data = self.cleaned_data["ip"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ ip")
        return data




class EditMachineForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de la machine")
    ip = forms.CharField(required=True, label="IP de la machine")
    vlan = forms.CharField(required=True, label="Vlan de la machine")
    maj = forms.CharField(required=True, label="Nom du modificateur")
    user = forms.CharField(required=True, label="Utilisateur de la machine")



    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) >20 :
            raise ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_ip(self):
        data = self.cleaned_data["ip"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ ip")
        return data

    def clean_vlan(self):
        data = self.cleaned_data["vlan"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ vlan")
        return data
    
    def clean_maj(self):
        data = self.cleaned_data["maj"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ maj")
        return data

    def clean_user(self):
        data = self.cleaned_data["user"]
        if len(data) >20 :
            raise ValidationError("Erreur de format pour le champ user")
        return data




class AddUtilisateurForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de l'utilisateur")
    prenom = forms.CharField(required=True, label="Prenom de l'utilisateur")
    secteur = forms.CharField(required=True, label="Secteur de l'utilisateur")

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) >20:
            raise ValidationError("Erreur de format pour le champ prenom")
        return data

    def clean_nom (self):
        data = self.cleaned_data["nom"]
        if len(data) >20:
            raise ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_secteur (self):
        data = self.cleaned_data["secteur"]
        if len(data) >20:
            raise ValidationError("Erreur de format pour le champ secteur")
        return data


class DelMachineForm(forms.Form):
    selected_machine = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )






class DelUtilisateurForm(forms.Form):
    selected_utilisateur = forms.ModelMultipleChoiceField(
        queryset=Utilisateur.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )


class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_prenom(self):
        data = self.cleaned_data["name"]
        if len(data) >100:
            raise ValidationError("Erreur de format pour le champ name")
        return data

    def clean_email (self):
        data = self.cleaned_data["email"]
        if len(data) >50:
            raise ValidationError("Erreur de format pour le champ email")
        return data
    
    def clean_message (self):
        data = self.cleaned_data["message"]
        if len(data) >200:
            raise ValidationError("Erreur de format pour le champ message")
        return data
    




class EditUtilisateurForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de l'utilisateur")
    prenom = forms.CharField(required=True, label="Prénom de l'utilisateur")
    secteur = forms.CharField(required=True, label="Secteur de l'utilisateur")
    majU = forms.CharField(required=True, label="Nom du modificateur")




    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) >20 :
            raise ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ prenom")
        return data

    def clean_secteur(self):
        data = self.cleaned_data["secteur"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ secteur")
        return data
    
    def clean_majU(self):
        data = self.cleaned_data["majU"]
        if len(data) >32 :
            raise ValidationError("Erreur de format pour le champ majU")
        return data








class DelContactMessageForm(forms.Form):
    selected_contact_message = forms.ModelMultipleChoiceField(
        queryset=ContactMessage.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )