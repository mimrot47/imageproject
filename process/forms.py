from .models import Uplod
from django import forms

class formUplod(forms.ModelForm):
    class Meta:
        model=Uplod
        fields='__all__'
        widgets={'image':forms.FileInput(attrs={'class':'form-control','type':'file'}),
        'action':forms.Select(attrs={'class':'form-control'}),}

