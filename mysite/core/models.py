from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    knows_math = models.BooleanField(default=False, null=False)
    knows_singing = models.BooleanField(default=False, null=False)
    knows_music = models.BooleanField(default=False, null=False)
    knows_drawing = models.BooleanField(default=False, null=False)
    knows_video_editing = models.BooleanField(default=False, null=False)
    knows_animation = models.BooleanField(default=False, null=False)
    learn_math = models.BooleanField(default=False, null=False)
    learn_singing = models.BooleanField(default=False, null=False)
    learn_music = models.BooleanField(default=False, null=False)
    learn_drawing = models.BooleanField(default=False, null=False)
    learn_video_editing = models.BooleanField(default=False, null=False)
    learn_animation = models.BooleanField(default=False, null=False)
    description = models.TextField(default="I love to learn and teach!", null=False)
    link = models.UUIDField(default=uuid.uuid4, unique=True, null=False)  # To create a URL to view a person's profile

