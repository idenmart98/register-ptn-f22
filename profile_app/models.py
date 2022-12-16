from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(blank=True,null=True, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class ConfirmLink(models.Model):
    uid = models.CharField(max_length=50)
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)