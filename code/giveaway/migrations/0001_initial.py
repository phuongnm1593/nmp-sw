# Generated by Django 3.1.3 on 2020-11-20 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('race_name', models.CharField(max_length=255)),
                ('server', models.CharField(choices=[('asia', 'asia'), ('global', 'global')], default='asia', max_length=8)),
                ('account_created_at', models.DateTimeField()),
                ('account_level', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.roll')),
            ],
        ),
    ]
