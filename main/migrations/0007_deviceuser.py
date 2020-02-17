# Generated by Django 3.0.3 on 2020-02-17 03:25
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("main", "0006_devicelink")]

    operations = [
        migrations.CreateModel(
            name="DeviceUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("public_key", models.TextField()),
            ],
            options={"abstract": False},
        )
    ]
