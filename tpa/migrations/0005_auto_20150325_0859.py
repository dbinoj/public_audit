# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpa', '0004_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditrequest',
            name='client_message',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auditrequest',
            name='server_message',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
