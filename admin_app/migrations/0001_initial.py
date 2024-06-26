# Generated by Django 5.0.6 on 2024-05-28 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Draft', 'Draft')], max_length=10)),
                ('star_rating', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupancy', models.PositiveIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.hotel')),
            ],
        ),
    ]
