# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from user_accounts.models import Profile

# @receiver(post_save, sender = User)
# def create_profile(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()


# No need of signals.py. Because i am creating user using User and Profile modles at the sametime.
# This Signals only allow add Profile object after creating User object. Both models handled in views.