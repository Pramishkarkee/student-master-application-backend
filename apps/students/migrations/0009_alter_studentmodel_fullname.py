# Generated by Django 3.2.6 on 2021-11-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_studentmodel_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='fullname',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]