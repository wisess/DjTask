# Generated by Django 3.1.7 on 2021-02-22 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0006_auto_20210222_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
