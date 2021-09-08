from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.models import USStateField

# Create your models here.
class CustomUser(AbstractUser):
    state = USStateField(null=True, default='OR')
    address1 = models.CharField(null=True, blank=True, max_length=255)
    address2 = models.CharField(null=True, blank=True, max_length=255)
    zip = models.CharField(null=True, max_length=5, default='97217')
    lat = models.CharField(null=True, blank=True, max_length=10)
    lon = models.CharField(null=True, blank=True, max_length=10)

    def __str__(self) -> str:
        return self.username