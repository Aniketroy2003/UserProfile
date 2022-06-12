from django.dispatch import receiver
from .models.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def createProfile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
            print("-----------------------creation successful------------------")


# post_save.connect(createProfile,sender=User)