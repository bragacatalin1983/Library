# Generated by Django 3.0.6 on 2020-06-29 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginait', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursit',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 29, 13, 55, 33, 826572)),
        ),
    ]