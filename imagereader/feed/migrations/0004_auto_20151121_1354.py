# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_image_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='min_height',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='source',
            name='min_width',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
