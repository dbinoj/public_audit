# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20150323_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemeta',
            name='aes_key',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
