from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class FileMeta(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True)
    storage_file_id = models.IntegerField(editable=False, null=True)
    name = models.CharField(max_length=200)
    size = models.BigIntegerField(editable=False)
    private_key = models.TextField(editable=False)
    aes_key = models.BinaryField(editable=False, null=True)
    hash_sha1 = models.CharField(max_length=160, editable=False)
    hash_md5 = models.CharField(max_length=32, editable=False)
    signature = models.TextField(editable=False)
    ts = models.DateTimeField(auto_now_add=True, null=True)

    def get_audit_result(self):
        try:
            fileaudit = FileAudit.objects.get(file_id=self)
        except FileAudit.DoesNotExist:
            fileaudit = None
        if fileaudit is not None:
            return fileaudit.result
        return ""

    def __str__(self):
        #return 'File Name: %s, User: %s' % self.name % self.user
        return 'File Name: %s' % self.name

class FileAudit(models.Model):
    file_id = models.ForeignKey(FileMeta)
    request_ts = models.DateTimeField(auto_now_add=True)
    response_ts = models.DateTimeField(null=True)
    result = models.CharField(default="Waiting for result...",max_length=200)

class User(AbstractUser):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    REQUIRED_FIELDS = ['user', 'name']
        

