# Generated by Django 3.2.6 on 2021-12-28 08:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('first_language', models.BooleanField(default=False)),
                ('speak', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('spoken_at_home', models.BooleanField(default=False)),
            ],
        ),
    ]
