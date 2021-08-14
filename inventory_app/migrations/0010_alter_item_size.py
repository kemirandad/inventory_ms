# Generated by Django 3.2.6 on 2021-08-14 01:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0009_auto_20210813_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), null=True, size=8),
        ),
    ]