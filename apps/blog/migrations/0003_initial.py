# Generated by Django 3.2.6 on 2022-05-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituteblog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.instituteuser'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.relation'),
        ),
    ]