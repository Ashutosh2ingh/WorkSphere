from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User


@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            group = Group.objects.get(name='SuperAdmin')
        elif instance.role == 'hr':
            group = Group.objects.get(name='HR')
        else:
            group = Group.objects.get(name='Employee')

        instance.groups.add(group)