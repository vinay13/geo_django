# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=77, blank=True)),
                ('email', models.CharField(max_length=47, blank=True)),
                ('phone_no', models.CharField(max_length=17, blank=True)),
                ('language', models.CharField(max_length=17, blank=True)),
                ('Currency', models.CharField(max_length=132, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80, blank=True)),
                ('price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('provider', models.ForeignKey(to='provider.Providers', related_name='service_areas')),
            ],
        ),
    ]
