from django.contrib import admin
from .models import Usuario, Especialidad, CentroMedico, Paciente, Medico, Cita

admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(CentroMedico)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)