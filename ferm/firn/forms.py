from django import forms
from django.forms import NumberInput,HiddenInput
from .models import Item

class QtdForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    quantidade = forms.IntegerField(label='Quantidade',min_value=1)

    