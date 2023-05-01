from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


from django.dispatch import receiver 
from django.urls import reverse 
from django_rest_passwordreset.signals import reset_password_token_created 
from django.core.mail import send_mail   



class GestionUtilisateur(BaseUserManager):
     
     def create_superuser(self, email, first_name, last_name, password, **other_fields):
          
          other_fields.setdefault('is_staff', True)
          other_fields.setdefault('is_superuser', True)
          other_fields.setdefault('is_active', True)
          
          if other_fields.get('is_staff') is not True:
               raise ValueError('le super utilisateur doit avoir son is_staff=True')
          
          if other_fields.get('is_superuser') is not True:
               raise ValueError('le super utilisateur doit avoir son is_superuser=True')
     
          return self.create_user(email, first_name, last_name, password, **other_fields)
     
     
     def create_user(self, email, first_name, last_name, password, **other_fields):
          
          if not email:
               raise ValueError(_("l'utilisateur doit avoir son email"))
          
          user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **other_fields)
          user.set_password(password)
          user.save()
          return user



class NouveauUtilisateur(AbstractBaseUser, PermissionsMixin):
     email = models.EmailField(_('email address'), unique=True)
     first_name = models.CharField(max_length=150)
     last_name = models.CharField(max_length=150, blank=True)
     start_date = models.DateTimeField(default=timezone.now)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)

     objects = GestionUtilisateur()

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['last_name', 'first_name']

     def __str__(self):
          return self.first_name




@receiver(reset_password_token_created) 
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs): 
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), 
                                                  reset_password_token.key) 
    send_mail( 
        # title : 
        "Réinitialisation du mot de passe pour {title}".format(title="Un site Web titre"), 
        # message : 
        email_plaintext_message, 
        # de : 
        " noreply@somehost.locale ",
        # à : 
        [reset_password_token.user.email] 
)