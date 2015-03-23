from django.db import models

# Create your models here.

class ClientFile(models.Model):
    # file_id = models.ForeignKey('client.FileMeta', null=True) # not needed cos its refered from client's FileMeta
    name = models.CharField(max_length=200)
    size = models.BigIntegerField(editable=False)
    blocks = models.IntegerField(editable=False)
    signature = models.TextField(editable=False)
    ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'File Name: %s, User: %s' % self.name % self.user

class FileBlock(models.Model):
    file_id = models.ForeignKey(ClientFile)
    path = models.FilePathField()
    tag_id = models.TextField(editable=False)
    hash_sha1 = models.TextField(editable=False)
    hash_md5 = models.TextField(editable=False)
    block_size = models.BigIntegerField(editable=False)

class AuditResponse(models.Model):
    file_id = models.ForeignKey(ClientFile)
    request_ts = models.DateTimeField(auto_now_add=True)
    response_ts = models.DateTimeField(null=True)
    result = models.CharField(default="Waiting for result...",max_length=200)

