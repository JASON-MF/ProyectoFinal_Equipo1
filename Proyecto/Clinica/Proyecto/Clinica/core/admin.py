from django.contrib import admin
from .models import Paciente, Medico, Cita, Especialidad, CentroMedico

admin.site.register(Especialidad)
admin.site.register(CentroMedico)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)