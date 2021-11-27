# Generated by Django 3.2.6 on 2021-11-27 10:41

import apps.core.fields
import apps.core.validators
import apps.students.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=250)),
                ('contact', apps.core.fields.PhoneNumberField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('image', models.ImageField(default='student/image/default_logo.png', upload_to=apps.students.utils.upload_student_image_to, validators=[apps.core.validators.ImageValidator()])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.studentuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemporaryAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('state_provision', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('country', models.CharField(max_length=200)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.studentmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('state_provision', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('country', models.CharField(max_length=200)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.studentmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
