from django import forms
from .models import Tutoria

class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        # Definimos qué campos llenará el usuario
        fields = ['asignatura', 'tema', 'fecha', 'modalidad', 'cupos']
        
        # Le damos estilo Bootstrap a los inputs
        widgets = {
            'asignatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cálculo I'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'cupos': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }