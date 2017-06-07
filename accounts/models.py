from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

class Profile(TimeStamp):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text=_("Optional, Maximum of 20 digits"),
        verbose_name=_("Phone Number")
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
