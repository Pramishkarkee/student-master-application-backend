# Generated by Django 3.2.6 on 2021-12-28 08:54

import apps.core.fields
import apps.core.generics
import apps.core.validators
import apps.institute.mixins
import apps.institute.utils
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=250)),
                ('contact', apps.core.fields.PhoneNumberField(max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('university', models.CharField(blank=True, max_length=200)),
                ('established', models.DateField(default=datetime.datetime.now, validators=[apps.institute.utils.past_date])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(default='institute/logo/default_logo.png', upload_to=apps.institute.utils.upload_institute_logo_to, validators=[apps.core.validators.ImageValidator()])),
                ('cover_image', models.ImageField(default='institute/cover_image/default_cover_image.png', upload_to=apps.institute.utils.upload_institute_cover_image_to, validators=[apps.core.validators.ImageValidator()])),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequiredDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('photo', models.BooleanField()),
                ('citizenship', models.BooleanField()),
                ('passport', models.BooleanField()),
                ('academic_certificate', models.BooleanField()),
                ('sop', models.BooleanField()),
                ('lor', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailInstituteView',
            fields=[
                ('institute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='institute.institute')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.core.generics.RetrieveAPIView, 'institute.institute', apps.institute.mixins.InstituteMixins),
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(choices=[('facebook', 'facebook'), ('youtube', 'youtube'), ('linkdin', 'linkdin'), ('instagram', 'instagram')], max_length=100)),
                ('link', models.URLField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.institute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteStaff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('profile_photo', models.ImageField(default='institute_staff/photo/default_logo.png', upload_to=apps.institute.utils.upload_institute_staff_image_to, validators=[apps.core.validators.ImageValidator()])),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.institute')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffposition')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.instituteuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteScholorship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('topic', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.institute')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
