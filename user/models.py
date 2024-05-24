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
    verified = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=timezone.now)
    last_seen_show = models.BooleanField(default=True)  

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name if self.first_name != '' else self.username

    def get_absolute_url(self):
        return reverse("USer_detail", kwargs={"pk": self.pk})
    
    def get_last_seen(self):
        if self.last_seen_show == False:
            return "last seen recently"
        else:
            return self.last_seen
