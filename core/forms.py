from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Paciente, Medico, Cita, Usuario

# Formulario para Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'fecha_nacimiento', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulario para Médico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'id_especialidad', 'telefono', 'id_centro']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_especialidad': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'id_centro': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulario para Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['id_paciente', 'id_medico', 'fecha', 'hora', 'motivo', 'estado']
        widgets = {
            'id_paciente': forms.Select(attrs={'class': 'form-control'}),
            'id_medico': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulario de Registro con modelo Usuario personalizado
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label="Dirección", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    telefono = forms.CharField(label="Teléfono", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "direccion", "fecha_nacimiento", "telefono"]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.direccion = self.cleaned_data.get('direccion')
        user.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        user.telefono = self.cleaned_data.get('telefono')

        if commit:
            user.save()
            grupo_clientes = Group.objects.filter(name="Clientes").first()
            if grupo_clientes:
                user.groups.add(grupo_clientes)

        return user