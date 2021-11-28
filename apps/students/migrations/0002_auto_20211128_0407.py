# Generated by Django 3.2.6 on 2021-11-28 04:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permanentaddress',
            name='nationality',
            field=models.CharField(choices=[('afghan', 'Afghan'), ('albanian', 'Albanian'), ('Algerian', 'Algerian'), ('Argentinian', 'Argentinian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Bangladeshi', 'Bangladeshi'), ('Belgian', 'Belgian'), ('Bolivian', 'Bolivian'), ('Batswana', 'Batswana'), ('nepales', 'nepalies'), ('indian', 'indian')], default='nepales', max_length=20),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='male', max_length=20),
        ),
        migrations.CreateModel(
            name='CompleteProfileTracker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('complete_address', models.BooleanField()),
                ('complete_academic_detail', models.BooleanField()),
                ('complete_parents_detail', models.BooleanField()),
                ('complete_citizenship_detail', models.BooleanField()),
                ('complete_passport_field', models.BooleanField()),
                ('complete_sop_field', models.BooleanField()),
                ('complete_personalessay_field', models.BooleanField()),
                ('complete_lor_field', models.BooleanField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.studentmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]