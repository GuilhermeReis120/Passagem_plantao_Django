# Formulário para PassagemPlantao e CentralMonitoramento
from django import forms
from .models_plantao import PassagemPlantao, CentralMonitoramento

class PassagemPlantaoForm(forms.ModelForm):
    class Meta:
        model = PassagemPlantao
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'class': 'input'}),
        }

class CentralMonitoramentoForm(forms.ModelForm):
    class Meta:
        model = CentralMonitoramento
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'observacoes': forms.Textarea(attrs={'rows': 3, 'class': 'input'}),
        }
