from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Roles(models.TextChoices):
        REGULAR = "regular", "Regular"
        MANAGER = "manager", "Manager"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length = 20,
        choices = Roles.choices,
        default = Roles.REGULAR,
    )

    def is_manager(self):
        return self.role == self.Roles.MANAGER
    
    def is_admin(self):
        return self.role == self.Roles.ADMIN
