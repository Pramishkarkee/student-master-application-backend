# Generated by Django 3.2.6 on 2021-10-29 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_booking_is_booked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counsellingschedule',
            old_name='counselor',
            new_name='counsellor',
        ),
    ]