# Generated by Django 3.0.5 on 2020-06-29 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginait', '0002_auto_20200629_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursit',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 29, 14, 29, 46, 786567)),
        ),
    ]