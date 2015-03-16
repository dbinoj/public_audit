# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_ts', models.DateTimeField(auto_now_add=True)),
                ('response_ts', models.DateTimeField(null=True)),
                ('result', models.CharField(default=b'Waiting for result...', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('size', models.BigIntegerField(editable=False)),
                ('blocks', models.IntegerField(editable=False)),
                ('signature', models.TextField(editable=False)),
                ('ts', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FilePathField()),
                ('tag_id', models.TextField(editable=False)),
                ('hash_sha1', models.TextField(editable=False)),
                ('hash_md5', models.TextField(editable=False)),
                ('size', models.BigIntegerField(editable=False)),
                ('file_id', models.ForeignKey(to='storage.ClientFile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='auditresponse',
            name='file_id',
            field=models.ForeignKey(to='storage.ClientFile'),
            preserve_default=True,
        ),
    ]
