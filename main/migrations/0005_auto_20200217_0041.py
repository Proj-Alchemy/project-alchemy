# Generated by Django 3.0.3 on 2020-02-17 00:41
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("main", "0004_auto_20200217_0008")]

    operations = [
        migrations.AddField(
            model_name="templatefragment",
            name="group",
            field=models.CharField(blank=True, default="", max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="templatefragment",
            name="template_text",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
