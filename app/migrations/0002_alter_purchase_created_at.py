# Generated by Django 5.0.4 on 2024-04-20 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 20, 13, 15, 30, 839190, tzinfo=datetime.timezone.utc)),
        ),
    ]