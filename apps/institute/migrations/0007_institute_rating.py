# Generated by Django 3.2.6 on 2022-04-27 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_alter_institute_institute_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='rating',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
