# Generated by Django 3.1.3 on 2020-12-02 03:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201015_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 3, 19, 59, 349152, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
