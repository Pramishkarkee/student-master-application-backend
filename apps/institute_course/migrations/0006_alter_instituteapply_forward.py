# Generated by Django 3.2.6 on 2021-12-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute_course', '0005_alter_instituteapply_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituteapply',
            name='forward',
            field=models.BooleanField(default=False),
        ),
    ]