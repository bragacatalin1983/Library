# Generated by Django 3.0.5 on 2020-05-07 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200507_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 7, 14, 10, 8, 530200)),
        ),
    ]