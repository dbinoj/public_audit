# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_clientfile_file_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientfile',
            name='file_id',
        ),
    ]
