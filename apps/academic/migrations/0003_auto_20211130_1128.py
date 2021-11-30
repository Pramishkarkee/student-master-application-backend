# Generated by Django 3.2.6 on 2021-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_alter_academic_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='academic',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='academic',
            constraint=models.UniqueConstraint(fields=('student', 'level'), name='student academic'),
        ),
    ]