from django.contrib.auth.models import User
from django.db.models.signals import pos_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(pos_save, sender=User)
def create_Token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    