# Generated by Django 3.2.12 on 2022-04-14 02:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0003_default_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 2, 55, 4, 546747, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
