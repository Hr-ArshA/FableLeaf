from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from extention.name_fixer import upload_img_path
from django.shortcuts import reverse

from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=20)
    profile_photo = models.ImageField(verbose_name='profile photo', upload_to=upload_img_path)
    bio = models.CharField(max_length=512)
    

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("USer_detail", kwargs={"pk": self.pk})
