# Generated by Django 3.2.6 on 2022-02-18 12:31

import apps.blog.utils
import apps.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_instituteblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituteblog',
            name='image',
            field=models.ImageField(default='institute/blog/default_logo.png', upload_to=apps.blog.utils.upload_blog_image_to, validators=[apps.core.validators.ImageValidator()]),
        ),
    ]