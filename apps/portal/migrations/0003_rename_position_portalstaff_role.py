# Generated by Django 3.2.6 on 2021-10-01 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_portalstaff_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portalstaff',
            old_name='position',
            new_name='role',
        ),
    ]