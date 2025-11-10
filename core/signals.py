from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario

@receiver(post_save, sender=User)
def crear_o_actualizar_usuario(sender, instance, created, **kwargs):
    if created:
        # Crear perfil extendido al crear el usuario
        Usuario.objects.create(
            username=instance.username,
            email=instance.email,
            auth_user=instance
        )
    else:
        # Intentar actualizar el perfil si existe, o crearlo si no
        usuario, creado = Usuario.objects.get_or_create(auth_user=instance)
        usuario.username = instance.username
        usuario.email = instance.email
        usuario.save()