from django import forms
from . import models

class tccform(forms.ModelForm):
    class Meta:
        model = models.Tcc
        fields = '__all__'
