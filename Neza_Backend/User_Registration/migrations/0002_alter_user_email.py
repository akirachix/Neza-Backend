# Generated by Django 4.2.5 on 2023-09-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
