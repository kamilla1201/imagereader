# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='source',
            field=models.URLField(default='', verbose_name=b'Source'),
            preserve_default=False,
        ),
    ]
