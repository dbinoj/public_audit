# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileblock',
            old_name='size',
            new_name='block_size',
        ),
    ]
