# Generated by Django 3.2.6 on 2021-10-28 11:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultancy', '0002_consultancystaff_user'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounsellingSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('end_time', models.TimeField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('BUSY', 'Busy'), ('UNAVAILABLE', 'Unavailable')], max_length=20)),
                ('counsellor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultancy.consultancystaff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('note', models.TextField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.counsellingschedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.studentuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
