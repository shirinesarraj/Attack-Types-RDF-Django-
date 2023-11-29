
# Create your models here.
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.EmailField(unique=True)