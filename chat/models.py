from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from extention.name_fixer import upload_img_path
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from uuid import uuid4

from django.utils.translation import gettext_lazy as _

# Create your models here.


class Conversation(models.Model):
    class TYPE(models.IntegerChoices):
        private = 1
        group = 2
        channel = 3
    Conversation_id = models.UUIDField(default=uuid4)
    displayـname = models.CharField(max_length=128)
    link = models.CharField(max_length=32)
    is_private = models.BooleanField(default=True)
    chat_type = models.IntegerField(choices=TYPE)
    profile_photo = models.ImageField(upload_to=upload_img_path)
    description = models.CharField(max_length=512)
    members = models.ManyToManyField(get_user_model(), related_name='memeber')
    extra_details = models.TextField(blank=True)
    

    class Meta:
        verbose_name = _("Conversation")
        verbose_name_plural = _("Conversations")

    def __str__(self):
        return str(self.Conversation_id)

    def get_absolute_url(self):
        return reverse("Conversation_detail", kwargs={"pk": self.pk})



class Message(models.Model):
    class TYPE(models.IntegerChoices):
        text = 1
        gif = 2
        voice = 3
        pic = 4
        video = 5
        music = 6

    # message_id = models.IntegerField()
    from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    chat_id = models.ManyToManyField(Conversation, related_name='message')
    created = models.DateField(auto_now_add=True)
    msg_type = models.IntegerField(choices=TYPE, default=1)
    # reactions = models.CharField(choices=REACT)
    content = models.TextField()
    is_edited = models.BooleanField(default=False)
    is_forwarded = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    seens = models.ManyToManyField(get_user_model(), through="Seen", related_name='seen', blank=True)


    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})
  


class Seen(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = _("Seen")
        verbose_name_plural = _("Seens")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("Seen_detail", kwargs={"pk": self.pk})


# class Reaction(models.Model):

    

#     class Meta:
#         verbose_name = _("Reaction")
#         verbose_name_plural = _("Reactions")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Reaction_detail", kwargs={"pk": self.pk})

