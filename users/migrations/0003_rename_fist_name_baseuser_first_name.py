# Generated by Django 4.1.5 on 2023-01-22 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_baseuser_middle_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseuser',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
