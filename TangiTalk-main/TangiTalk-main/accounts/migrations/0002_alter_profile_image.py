# Generated by Django 4.2.2 on 2023-07-02 14:01

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, upload_to=accounts.models.get_profile_image_upload_path
            ),
        ),
    ]
