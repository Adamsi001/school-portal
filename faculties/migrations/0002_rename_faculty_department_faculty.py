# Generated by Django 4.1.5 on 2023-02-04 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='Faculty',
            new_name='faculty',
        ),
    ]
