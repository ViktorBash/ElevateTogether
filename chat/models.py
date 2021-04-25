from django.db import models
from django.contrib.auth.models import User
import uuid

# # Create your models here.
class Connection(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=False),
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False),
    blocked = models.BooleanField(default=False, null=False),
    accepted = models.BooleanField(default=False, null=False),
    link = models.UUIDField(default=uuid.uuid4, unique=True, null=False),
