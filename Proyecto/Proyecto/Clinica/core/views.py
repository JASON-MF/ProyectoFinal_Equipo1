from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm

# Paciente
class PacienteListView(ListView):
    model = Paciente
    template_name = 'core/paciente/list.html'
    context_object_name = 'pacientes'
    paginate_by = 15

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'core/paciente/confirm_delete.html'
    success_url = reverse_lazy('core:paciente_list')

# Medico
class MedicoListView(ListView):
    model = Medico
    template_name = 'core/medico/list.html'
    context_object_name = 'medicos'
    paginate_by = 15

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('core:medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'core/medico/form.html'
    success_url = reverse_lazy('core:medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'core/medico/confirm_delete.html'
    success_url = reverse_lazy('core:medico_list')

# Cita
class CitaListView(ListView):
    model = Cita
    template_name = 'core/cita/list.html'
    context_object_name = 'citas'
    paginate_by = 20

class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'core/cita/form.html'
    success_url = reverse_lazy('core:cita_list')

class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'core/cita/form.html'
    success_url = reverse_lazy('core:cita_list')

class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'core/cita/confirm_delete.html'
    success_url = reverse_lazy('core:cita_list')