# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bondservice_app', '0002_auto_20170103_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bond',
            name='payFrequency',
        ),
        migrations.AddField(
            model_name='bond',
            name='paymentsPerYear',
            field=models.IntegerField(default=2),
        ),
    ]
