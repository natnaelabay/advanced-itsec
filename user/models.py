import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

'''
python manage.py shell

from user.models import User
User.objects.create_superuser(email='admin@admin.com', password='123123')

'''

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, auto_created=True)
   
    username = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=200)
    first_name = None
    last_name = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    class Meta:
        ordering = ['-id']