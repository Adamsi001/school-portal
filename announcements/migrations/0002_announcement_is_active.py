# Generated by Django 4.1.5 on 2023-01-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]