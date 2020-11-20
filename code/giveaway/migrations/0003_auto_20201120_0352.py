# Generated by Django 3.1.3 on 2020-11-20 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0002_auto_20201120_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='roll_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='SessionKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('expired_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.candidate')),
            ],
        ),
    ]
