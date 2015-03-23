from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class FileMeta(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True)
    storage_file_id = models.IntegerField(editable=False, null=True)
    name = models.CharField(max_length=200)
    size = models.BigIntegerField(editable=False)
    private_key = models.TextField(editable=False)
    hash_sha1 = models.CharField(max_length=160, editable=False)
    hash_md5 = models.CharField(max_length=32, editable=False)
    signature = models.TextField(editable=False)
    ts = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'File Name: %s, User: %s' % self.name % self.user

class FileAudit(models.Model):
    file_id = models.ForeignKey(FileMeta)
    request_ts = models.DateTimeField(auto_now_add=True)
    response_ts = models.DateTimeField(null=True)
    result = models.CharField(default="Waiting for result...",max_length=200)

