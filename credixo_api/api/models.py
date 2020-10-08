
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
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
    group = models.ForeignKey(Group,on_delete=models.CASCADE,default=3)

"""
using the signal for passing the function.
"""
@receiver(reset_password_token_created)
def password_reset_token_created(sender,instance,reset_password_token,*args,**kwargs):
    """
    The format of the mail sent for the password reset mail
    """
    
    email_plaintext_message="The Password reset token is {}?token={}".format(reverse('password_reset:reset-password-request'),reset_password_token.key)
    # send_mail
    subject = "Password Reset for {title}".format(title="Credixo")
    message = email_plaintext_message
    from_email = settings.EMAIL_HOST_USER
    recipient_list=["surendersingh1995nov@gmail.com"]
    send_mail( subject, message, from_email, recipient_list )