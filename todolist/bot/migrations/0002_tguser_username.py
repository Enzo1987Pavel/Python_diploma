# Generated by Django 4.1.3 on 2022-12-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tguser",
            name="username",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="TG USERNAME",
            ),
        ),
    ]
