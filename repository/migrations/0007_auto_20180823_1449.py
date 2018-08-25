# Generated by Django 2.1 on 2018-08-23 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_phone',
            field=models.CharField(default=datetime.datetime(2018, 8, 23, 6, 49, 14, 186361, tzinfo=utc), max_length=12),
            preserve_default=False,
        ),
    ]