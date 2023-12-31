# Generated by Django 4.1.5 on 2023-02-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_baseuser_options'),
        ('courses', '0011_alter_course_lecturers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lecturers',
            field=models.ManyToManyField(related_name='+', to='users.lecturer'),
        ),
    ]
