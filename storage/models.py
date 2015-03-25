from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class ClientFile(models.Model):
    # file_id = models.ForeignKey('client.FileMeta', null=True) # not needed cos its refered from client's FileMeta
    user = models.ForeignKey(AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=200)
    size = models.BigIntegerField(editable=False)
    blocks = models.IntegerField(editable=False, null=True)
    signature = models.TextField(editable=False)
    ts = models.DateTimeField(auto_now_add=True)

    def get_audit_result(self):
        try:
            auditresponse = AuditResponse.objects.get(file_id=self)
        except AuditResponse.DoesNotExist:
            auditresponse = None
        if auditresponse is not None:
            return auditresponse.result
        return ""

    def __str__(self):
        return 'File Name: %s' % self.name

class FileBlock(models.Model):
    file_id = models.ForeignKey(ClientFile)
    path = models.FilePathField()
    tag_id = models.TextField(editable=False, null=True)
    hash_sha1 = models.TextField(editable=False)
    hash_md5 = models.TextField(editable=False)
    block_size = models.BigIntegerField(editable=False)
    signature = models.TextField(editable=False, null=True)

class AuditResponse(models.Model):
    file_id = models.ForeignKey(ClientFile)
    request_ts = models.DateTimeField(auto_now_add=True)
    response_ts = models.DateTimeField(null=True)
    result = models.CharField(default="Waiting for result...",max_length=200)

