from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.conf import settings


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "This is your token to reset your password={} \nKindly click on following link to reset your password. \n{}".format(reset_password_token.key, settings.RESETLINK)

    send_mail(
      # title:
      "Password Reset",
      # message:
      email_plaintext_message,
      # from:
      settings.EMAIL_HOST_USER,
      # to:
      [reset_password_token.user.email]
    )