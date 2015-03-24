# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_filemeta_aes_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemeta',
            name='aes_key',
            field=models.BinaryField(null=True),
            preserve_default=True,
        ),
    ]
