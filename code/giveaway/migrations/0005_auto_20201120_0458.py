# Generated by Django 3.1.3 on 2020-11-20 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0004_roll_ads_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionkey',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='giveaway.candidate'),
        ),
    ]