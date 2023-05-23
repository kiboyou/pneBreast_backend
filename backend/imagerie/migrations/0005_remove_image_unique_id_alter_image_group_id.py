# Generated by Django 4.1.4 on 2023-05-21 18:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("imagerie", "0004_alter_image_unique_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="unique_id",
        ),
        migrations.AlterField(
            model_name="image",
            name="group_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
