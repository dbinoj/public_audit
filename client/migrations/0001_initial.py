# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAudit',
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
            name='FileMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storage_file_id', models.IntegerField(editable=False)),
                ('name', models.CharField(max_length=200)),
                ('size', models.BigIntegerField(editable=False)),
                ('private_key', models.TextField(editable=False)),
                ('hash_sha1', models.CharField(max_length=160, editable=False)),
                ('hash_md5', models.CharField(max_length=32, editable=False)),
                ('signature', models.TextField(editable=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fileaudit',
            name='file_id',
            field=models.ForeignKey(to='client.FileMeta'),
            preserve_default=True,
        ),
    ]
