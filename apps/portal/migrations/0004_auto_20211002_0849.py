# Generated by Django 3.2.6 on 2021-10-02 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_rename_position_portalstaff_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portalstaff',
            name='portal',
        ),
        migrations.DeleteModel(
            name='Portal',
        ),
    ]