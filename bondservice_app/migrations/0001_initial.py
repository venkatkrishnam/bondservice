# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cusip', models.CharField(max_length=8)),
                ('issuer', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=10)),
                ('issueDate', models.DateTimeField()),
                ('maturityDate', models.DateTimeField()),
                ('parValue', models.DecimalField(max_digits=12, decimal_places=6)),
                ('coupon', models.DecimalField(max_digits=4, decimal_places=3)),
                ('paymentFrequency', models.CharField(default='Semi-Annual', max_length=20)),
                ('settlementDelay', models.CharField(default='2D', max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
