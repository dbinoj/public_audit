# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20150323_0927'),
        ('storage', '0002_auto_20150317_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientfile',
            name='file_id',
            field=models.ForeignKey(to='client.FileMeta', null=True),
            preserve_default=True,
        ),
    ]
