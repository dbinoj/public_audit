# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_clientfile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileblock',
            name='signature',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fileblock',
            name='tag_id',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
