# Generated by Django 3.2.6 on 2022-05-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20220503_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic',
            name='name',
            field=models.CharField(default='Academic Document', max_length=100),
        ),
    ]
