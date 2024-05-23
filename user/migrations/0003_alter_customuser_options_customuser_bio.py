# Generated by Django 5.0.6 on 2024-05-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_profile_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
