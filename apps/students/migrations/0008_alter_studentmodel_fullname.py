# Generated by Django 3.2.6 on 2021-11-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20211130_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='fullname',
            field=models.CharField(max_length=250),
        ),
    ]
