from django import forms
from .models import *


class BackForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = ('name', 'email', 'number', 'year')


class TestForm(forms.ModelForm):
    class Meta:
        model = Oplata
        fields = ('name', 'number', 'data', 'ccv')
