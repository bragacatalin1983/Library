# Generated by Django 3.0.6 on 2021-02-11 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210211_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 11, 15, 55, 53, 118221)),
        ),
    ]
