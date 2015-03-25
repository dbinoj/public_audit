# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpa', '0005_auto_20150325_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditrequest',
            name='client_message',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auditrequest',
            name='server_message',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auditrequest',
            name='storage_file_id',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
