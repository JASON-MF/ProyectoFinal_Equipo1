from django.db import models
from django.contrib.auth.models import User




class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campos adicionales del perfil
    direccion = models.CharField(max_length=255, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.auth_user.username


# Modelo de Especialidad médica


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


# Modelo de Centro Médico


class CentroMedico(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


# Modelo de Paciente


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


# Modelo de Médico


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    id_centro = models.ForeignKey(CentroMedico, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.id_especialidad or ''}"


# Modelo de Cita médica


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True)
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-hora']

    def __str__(self):
        return f"Cita {self.fecha} {self.hora} - {self.id_paciente}"