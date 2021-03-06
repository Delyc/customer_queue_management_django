# Generated by Django 4.0.4 on 2022-04-15 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_teller_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='teller',
            name='completion_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
