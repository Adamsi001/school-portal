# Generated by Django 4.1.5 on 2023-01-22 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_fist_name_baseuser_first_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
