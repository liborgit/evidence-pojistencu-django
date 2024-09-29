from django import forms
from .models import InsuredPerson

class InsuredPersonForm(forms.ModelForm):
    class Meta:
        model = InsuredPerson
        fields = ["first_name", "last_name", "age", "phone", "email"]
        labels = {
            "first_name": "Jméno",
            "last_name": "Příjmení",
            "age": "Věk",
            "phone": "Telefon",
            "email": "E-mail",
        }
