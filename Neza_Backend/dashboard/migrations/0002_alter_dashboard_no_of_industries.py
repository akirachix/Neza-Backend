# Generated by Django 4.2.5 on 2023-09-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='no_of_industries',
            field=models.IntegerField(default=0),
        ),
    ]
