from django import forms
from .models_cftv import PassageCFTV

class PassageCFTVForm(forms.ModelForm):
    class Meta:
        model = PassageCFTV
        fields = ['data', 'operador', 'base', 'nome_backoffice', 'observacoes']
