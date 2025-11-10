from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.PacienteListView.as_view(), name='index'),

    # Pacientes
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # Médicos
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/nuevo/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.MedicoDeleteView.as_view(), name='medico_delete'),

    # Citas
    path('citas/', views.CitaListView.as_view(), name='cita_list'),
    path('citas/nuevo/', views.CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:pk>/editar/', views.CitaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:pk>/eliminar/', views.CitaDeleteView.as_view(), name='cita_delete'),

    # Registro
    path('registro/', views.registro_view, name='registro'),
]