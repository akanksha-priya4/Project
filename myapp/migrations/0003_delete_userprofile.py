# Generated by Django 5.1.1 on 2024-09-22 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_userprofile_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
