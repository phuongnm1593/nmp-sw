# Generated by Django 3.1.3 on 2020-11-20 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0005_auto_20201120_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionkey',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 20, 5, 59, 41, 828345)),
        ),
    ]