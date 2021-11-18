# Generated by Django 3.2.6 on 2021-11-13 02:35

import apps.student.utils.file_function
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('college', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.studentuser')),
                ('contact', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='Male', max_length=30)),
                ('country', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('city_town', models.CharField(max_length=200)),
                ('state_provision', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('parents_isfull', models.BooleanField(default=False)),
                ('photo', models.FileField(blank=True, upload_to=apps.student.utils.file_function.student_photo, validators=[apps.student.utils.file_function.validate_file])),
            ],
        ),
        migrations.CreateModel(
            name='CitizenshipModel',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='student.student')),
                ('front_page', models.FileField(blank=True, upload_to=apps.student.utils.file_function.student_national_certificate)),
                ('back_page', models.FileField(blank=True, upload_to=apps.student.utils.file_function.student_national_certificate)),
            ],
        ),
        migrations.CreateModel(
            name='PassportModel',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='student.student')),
                ('passport', models.FileField(blank=True, upload_to=apps.student.utils.file_function.student_national_certificate)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEssay',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='student.student')),
                ('topic', models.CharField(max_length=300)),
                ('essay', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitedCollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
                ('first_name', models.CharField(default='pramish', max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(default='karki', max_length=200)),
                ('status', models.CharField(default='0', max_length=40)),
                ('applyed', models.BooleanField()),
                ('view_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('apply_date', models.DateTimeField(auto_now=True)),
                ('view', models.BooleanField(default=False)),
                ('student_action', models.CharField(choices=[('1', 'no_action'), ('2', 'cancle'), ('3', 'denied'), ('4', 'Admit')], default='1', max_length=6)),
                ('form_payment', models.BooleanField(default=False)),
                ('enrolled', models.BooleanField(default=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'unique_together': {('college', 'student')},
            },
        ),
        migrations.AddField(
            model_name='student',
            name='apply',
            field=models.ManyToManyField(through='student.StudentApply', to='college.College'),
        ),
        migrations.CreateModel(
            name='LORModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lor', models.FileField(blank=True, upload_to=apps.student.utils.file_function.student_certificate)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eligibility_exam_name', models.CharField(blank=True, max_length=600, null=True)),
                ('score', models.IntegerField()),
                ('certificate', models.FileField(upload_to=apps.student.utils.file_function.student_certificate)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentapply')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents_type', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=200)),
                ('relation', models.CharField(default='Father', max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'unique_together': {('relation', 'student')},
            },
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institute_name', models.CharField(max_length=200)),
                ('duration', models.CharField(default='1', max_length=40)),
                ('level', models.CharField(max_length=200)),
                ('percentage', models.FloatField()),
                ('outof', models.IntegerField(default=100)),
                ('marksheet', models.FileField(upload_to=apps.student.utils.file_function.student_certificate)),
                ('certificate', models.FileField(upload_to=apps.student.utils.file_function.student_certificate)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'unique_together': {('student', 'level')},
            },
        ),
    ]
