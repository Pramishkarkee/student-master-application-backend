# Generated by Django 3.2.6 on 2022-05-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutestaff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.instituteuser'),
        ),
        migrations.AddField(
            model_name='institutescholorship',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.institute'),
        ),
        migrations.AddField(
            model_name='addinstitutefacility',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='institute.facility'),
        ),
        migrations.AddField(
            model_name='addinstitutefacility',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_related', to='institute.institute'),
        ),
        migrations.AlterUniqueTogether(
            name='socialmedialink',
            unique_together={('institute', 'name')},
        ),
    ]