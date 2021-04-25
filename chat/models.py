from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Connection(models.Model):
    '''
    The Connection model holds the 2 people connected together, and the UUID portion of the link to a chat room for them. Blocked and accepted are also added as features
    '''
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentor", null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student", null=True)
    blocked = models.BooleanField(default=False, null=False)
    accepted = models.BooleanField(default=False, null=False)
    link = models.UUIDField(default=uuid.uuid4, unique=True, null=False)