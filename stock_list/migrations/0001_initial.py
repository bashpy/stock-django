# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moneycontrol',
            fields=[
                ('COMPANY', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('LTP', models.FloatField(max_length=10)),
                ('Change_I', models.CharField(max_length=7)),
                ('VOLUME', models.IntegerField(max_length=10)),
                ('BUY_PRICE', models.FloatField(max_length=7)),
                ('SELL_PRICE', models.FloatField(max_length=7)),
                ('BUY_QTY', models.FloatField(max_length=7)),
                ('SELL_QTY', models.FloatField(max_length=7)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'money_control',
            },
            bases=(models.Model,),
        ),
    ]
