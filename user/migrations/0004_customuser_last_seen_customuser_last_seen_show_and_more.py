# Generated by Django 5.0.6 on 2024-05-24 05:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_options_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_seen_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]