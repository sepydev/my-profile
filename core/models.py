from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", null=True, blank=True, verbose_name=_("Image"))
    bio = models.TextField(default="no bio...", max_length=300, verbose_name=_("Bio"))
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Country"))
    facebook = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Facebook"))
    instagram = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Instagram"))
    twitter = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Twitter"))
    linkedin = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Linkedin"))
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
