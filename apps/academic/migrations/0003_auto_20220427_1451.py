# Generated by Django 3.2.6 on 2022-04-27 14:51

import apps.academic.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20220218_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalessay',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalessay',
            name='essay',
            field=models.FileField(blank=True, null=True, upload_to=apps.academic.utils.upload_academic_doc_to),
        ),
    ]