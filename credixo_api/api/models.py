
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import Group
"""
Creating the Custom user Model to have the email authentication 
and also to have extra fields for deciding the group assigned
"""
class User(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=20)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
        
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    """
    Having three user levels Super-admin, Teacher, Student.
    Default is Student which is 3.
    """
    # group = models.ForeignKey(Group,on_delete=models.CASCADE,default=3)