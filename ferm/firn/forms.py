from django import forms
from django.forms import NumberInput
from .models import Item

class QtdForm(forms.ModelForm):
    # qtd = forms.ModelChoiceField(queryset=Item.objects.all())
    
    class Meta:
        model=Item
        fields=['quantidade']
        widgets= {
            'quantidade': NumberInput(attrs={'max':model.quantidade,'min':1})
        }