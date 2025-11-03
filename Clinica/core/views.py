from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm, RegistroUsuarioForm  # ← CAMBIO AQUÍ

# Vista de registro de usuarios con perfil extendido
def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)  # ← CAMBIO AQUÍ
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()  # ← CAMBIO AQUÍ
    return render(request, 'core/registro.html', {'form': form})

# Decorador para proteger vistas privadas
decoradores_login = [login_required]

# Paciente
@method_decorator(decoradores_login, name='dispatch')
class PacienteListView(ListView):
    model = Paciente
    template_name = 'core/paciente/list.html'
    context_object_name = 'pacientes'
    paginate_by = 15

@method_decorator(decoradores_login, name='dispatch')
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')

@method_decorator(decoradores_login, name='dispatch')
class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')

@method_decorator(decoradores_login, name='dispatch')
class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'core/paciente/confirm_delete.html'
    success_url = reverse_lazy('core:paciente_list')

# Médico
@method_decorator(decoradores_login, name='dispatch')
class MedicoListView(ListView):
    model = Medico
    template_name = 'core/medico/list.html'
    context_object_name = 'medicos'
    paginate_by = 15

@method_decorator(decoradores_login, name='dispatch')
class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('core:medico_list')

@method_decorator(decoradores_login, name='dispatch')
class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('core:medico_list')

@method_decorator(decoradores_login, name='dispatch')
class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'core/medico/confirm_delete.html'
    success_url = reverse_lazy('core:medico_list')

# Cita
@method_decorator(decoradores_login, name='dispatch')
class CitaListView(ListView):
    model = Cita
    template_name = 'core/cita/list.html'
    context_object_name = 'citas'
    paginate_by = 20

@method_decorator(decoradores_login, name='dispatch')
class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'core/cita/form.html'
    success_url = reverse_lazy('core:cita_list')

@method_decorator(decoradores_login, name='dispatch')
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'core/cita/form.html'
    success_url = reverse_lazy('core:cita_list')

@method_decorator(decoradores_login, name='dispatch')
class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'core/cita/confirm_delete.html'
    success_url = reverse_lazy('core:cita_list')