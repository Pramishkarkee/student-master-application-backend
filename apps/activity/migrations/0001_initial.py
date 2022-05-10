# Generated by Django 3.2.6 on 2022-05-10 13:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('position_lidership', models.CharField(blank=True, max_length=100, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
