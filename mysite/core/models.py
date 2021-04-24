from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    knows_math = models.BooleanField(default=False, null=False)
    knows_singing = models.BooleanField(default=False, null=False)
    knows_music = models.BooleanField(default=False, null=False)
    knows_drawing = models.BooleanField(default=False, null=False)
    knows_video_editing = models.BooleanField(default=False, null=False)
    knows_animation = models.BooleanField(default=False, null=False)
