# Generated by Django 3.1.3 on 2020-11-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='account_created_at',
            field=models.DateField(),
        ),
    ]
