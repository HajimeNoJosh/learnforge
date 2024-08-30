from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# # from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser, PermissionsMixin):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(_("email address"), unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  created_at = models.DateField(default=timezone.now)
  updated_at = models.DateField(default=timezone.now)
  REQUIRED_FIELDS = []

  def __str__(self):
    return f"{self.firstname} {self.lastname}"