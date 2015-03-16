from django.db import models

# Create your models here.

class AuditRequest(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    storage_file_id = models.IntegerField(editable=False)
    result = models.CharField(default="Auditing...")
