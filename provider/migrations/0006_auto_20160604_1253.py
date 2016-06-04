# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20160604_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='poly',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
