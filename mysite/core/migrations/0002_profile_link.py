# Generated by Django 3.1 on 2021-04-25 00:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='link',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]