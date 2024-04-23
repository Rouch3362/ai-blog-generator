from django.contrib.auth.signals import user_logged_in , user_logged_out
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def on_user_login(sender , request , **kwargs):
    messages.success(request , f"Welcome {request.user.username}")

@receiver(user_logged_out)
def on_user_logout(sender , request , **kwargs):
    messages.success(request , f"Bye {request.user.username}")
