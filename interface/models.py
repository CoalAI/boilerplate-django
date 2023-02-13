from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Custom fields example
	username = models.CharField(max_length=150, unique=True , null=True)
	# Required
	objects = EmailUserManager()