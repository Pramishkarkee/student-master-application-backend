# Generated by Django 3.2.6 on 2022-05-10 13:11

import apps.core.validators
import apps.gallery.utils
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='consultancy/logo/default_logo.png', upload_to=apps.gallery.utils.upload_gallery_image_to, validators=[apps.core.validators.ImageValidator()])),
            ],
            options={
                'db_table': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='InstituteGallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('approve', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='consultancy/logo/default_logo.png', upload_to=apps.gallery.utils.upload_gallery_image_to, validators=[apps.core.validators.ImageValidator()])),
            ],
            options={
                'db_table': 'institute_galleries',
            },
        ),
    ]
