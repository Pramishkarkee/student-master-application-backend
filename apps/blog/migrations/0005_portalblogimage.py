# Generated by Django 3.2.6 on 2022-04-26 15:38

import apps.blog.utils
import apps.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220426_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalBlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='institute/blog/default_logo.png', upload_to=apps.blog.utils.upload_blog_image_to, validators=[apps.core.validators.ImageValidator()])),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.portalblog')),
            ],
        ),
    ]