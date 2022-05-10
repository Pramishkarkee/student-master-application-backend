# Generated by Django 3.2.6 on 2022-05-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together={('student', 'name')},
        ),
    ]
