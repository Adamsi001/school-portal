# Generated by Django 4.1.5 on 2023-01-22 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_baseuser_options'),
        ('core', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lecturers',
            field=models.ManyToManyField(related_name='courses', to='users.lecturer'),
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('is_approved', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('courses', models.ManyToManyField(related_name='registrations', to='courses.course')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_registrations', to='core.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_registrations', to='users.student')),
            ],
            options={
                'verbose_name': 'Course Registration',
                'verbose_name_plural': 'Courses Registrations',
            },
        ),
    ]