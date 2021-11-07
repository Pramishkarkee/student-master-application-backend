# Generated by Django 3.2.6 on 2021-09-22 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('consultancy', '0002_consultancystaff_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultancystaff',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffposition'),
        ),
        migrations.DeleteModel(
            name='ConsultancyStaffPosition',
        ),
    ]
