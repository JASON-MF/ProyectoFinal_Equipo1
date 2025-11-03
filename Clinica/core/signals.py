from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario

@receiver(post_save, sender=User)
def crear_o_actualizar_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(username=instance.username, email=instance.email, auth_user=instance)
    else:
        try:
            usuario = instance.usuario
            usuario.username = instance.username
            usuario.email = instance.email
            usuario.auth_user = instance
            usuario.save()
        except Usuario.DoesNotExist:
            Usuario.objects.create(username=instance.username, email=instance.email, auth_user=instance)