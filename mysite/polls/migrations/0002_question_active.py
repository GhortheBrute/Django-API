# Generated by Django 5.1.4 on 2025-01-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
