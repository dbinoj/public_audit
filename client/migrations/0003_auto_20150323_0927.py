# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_filemeta_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemeta',
            name='storage_file_id',
            field=models.IntegerField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filemeta',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
