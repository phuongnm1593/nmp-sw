# Generated by Django 3.1.3 on 2020-11-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0003_auto_20201120_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='ads_url',
            field=models.CharField(default='ads_short_url', max_length=255),
        ),
    ]
