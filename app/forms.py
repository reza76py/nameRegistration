from django import forms
from app.models import Name

class Form(forms.ModelForm):
    class Meta: 
        model = Name
        fields = ['name', 'lastname', 'description']
    