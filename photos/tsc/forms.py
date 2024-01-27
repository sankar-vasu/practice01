from django import forms
from .models import Person_details

class Person_datails_form(forms.ModelForm):
    class Meta:
        model = Person_details
        fields = ('name','surname')

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Enter your name','color':'blue'})

        }
