# Generated by Django 4.1.5 on 2023-01-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]