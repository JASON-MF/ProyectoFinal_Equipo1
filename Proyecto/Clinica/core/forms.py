from django import forms
from .models import Paciente, Medico, Cita

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['id_usuario', 'nombre', 'fecha_nacimiento', 'direccion', 'telefono']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['id_usuario', 'nombre', 'id_especialidad', 'telefono', 'id_centro']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_especialidad': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'id_centro': forms.Select(attrs={'class': 'form-control'}),
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['id_paciente', 'id_medico', 'fecha', 'hora', 'motivo', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'id_paciente': forms.Select(attrs={'class': 'form-control'}),
            'id_medico': forms.Select(attrs={'class': 'form-control'}),
        }