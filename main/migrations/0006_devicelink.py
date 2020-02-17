# Generated by Django 3.0.3 on 2020-02-17 01:03
import uuid

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("main", "0005_auto_20200217_0041")]

    operations = [
        migrations.CreateModel(
            name="DeviceLink",
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
                ("port_a", models.CharField(max_length=100)),
                ("port_b", models.CharField(max_length=100)),
                ("ipv4_a", models.GenericIPAddressField()),
                ("ipv6_a", models.GenericIPAddressField()),
                ("ipv4_b", models.GenericIPAddressField()),
                ("ipv6_b", models.GenericIPAddressField()),
                ("ospf", models.BooleanField()),
                ("mpls", models.BooleanField()),
                (
                    "device_a",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_a",
                        to="main.Device",
                    ),
                ),
                (
                    "device_b",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_b",
                        to="main.Device",
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
