from django.db.models.signals import post_save
from django.contrib.auth.models import User #user will be sender
from django.dispatch import receiver
from user_auth.models import Profile

#Its main purpose is to create Profile instance for user right after user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #this function just creates Profile
    if created: #if User instance is created
        Profile.objects.create(user=instance) #this creates Profile instance

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #this function saves the profile
    instance.profile.save()

#check user_auth/apps.py where signals in imported
#also check user_auth/__init__.py
