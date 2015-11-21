# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20151121_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
