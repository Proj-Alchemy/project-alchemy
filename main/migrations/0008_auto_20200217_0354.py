# Generated by Django 3.0.3 on 2020-02-17 03:54
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("main", "0007_deviceuser")]

    operations = [
        migrations.RenameField(
            model_name="device", old_name="loopbackv4_address", new_name="loopbackv4"
        ),
        migrations.RenameField(
            model_name="device", old_name="loopbackv6_address", new_name="loopbackv6"
        ),
    ]
