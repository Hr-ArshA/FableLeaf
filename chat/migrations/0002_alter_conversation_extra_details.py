# Generated by Django 5.0.6 on 2024-05-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='extra_details',
            field=models.TextField(blank=True),
        ),
    ]
