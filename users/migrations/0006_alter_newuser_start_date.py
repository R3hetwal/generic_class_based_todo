# Generated by Django 4.1.6 on 2023-02-09 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 6, 13, 55, 776523, tzinfo=datetime.timezone.utc)),
        ),
    ]