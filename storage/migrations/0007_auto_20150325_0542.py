# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_auto_20150325_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientfile',
            name='blocks',
            field=models.IntegerField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
