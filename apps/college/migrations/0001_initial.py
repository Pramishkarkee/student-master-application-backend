# Generated by Django 3.2.6 on 2021-09-17 08:09

import apps.student.utils.file_function
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=40)),
                ('floor', models.CharField(max_length=20)),
                ('room_no', models.CharField(max_length=20)),
                ('room_type', models.CharField(choices=[('single', 'SINGLE'), ('sharing', 'SHARING')], max_length=200)),
                ('kitchen', models.CharField(choices=[('single', 'SINGLE'), ('sharing', 'SHARING'), ('Common Shaired Kitchen', 'COMMONSHAIREDKITCHEN')], max_length=200)),
                ('laundry', models.BooleanField()),
                ('internet', models.BooleanField()),
                ('attach_rest_room', models.BooleanField()),
                ('fan', models.BooleanField()),
                ('air_condition', models.BooleanField()),
                ('swimming_pool', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther', models.CharField(max_length=100)),
                ('institute_relation', models.CharField(choices=[('student', 'STUDENT'), ('employee', 'EMPLOYEE'), ('guest', 'GUEST')], max_length=100)),
                ('work_on', models.CharField(max_length=300)),
                ('post', models.CharField(max_length=200)),
                ('publish', models.DateField()),
                ('image', models.FileField(upload_to=apps.student.utils.file_function.content_file_name)),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
