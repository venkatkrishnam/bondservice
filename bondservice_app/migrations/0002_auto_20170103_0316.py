# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bondservice_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bond',
            old_name='paymentFrequency',
            new_name='payFrequency',
        ),
        migrations.RenameField(
            model_name='bond',
            old_name='settlementDelay',
            new_name='settleDelay',
        ),
        migrations.AlterField(
            model_name='bond',
            name='cusip',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='bond',
            name='issueDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bond',
            name='maturityDate',
            field=models.DateField(),
        ),
    ]
