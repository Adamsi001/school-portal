# Generated by Django 4.1.5 on 2023-02-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_baseuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_lecturer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_student_adviser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='staff_type',
            field=models.CharField(blank=True, choices=[('academic', 'academic'), ('non-academic', 'non-academic'), ('other', 'other')], max_length=30, null=True),
        ),
    ]
