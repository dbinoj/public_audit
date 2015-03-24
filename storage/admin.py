from django.contrib import admin



# Register your models here.
from . import models

admin.site.register(models.ClientFile)
admin.site.register(models.FileBlock)
admin.site.register(models.AuditResponse)
admin.site.site_title = 'Public_audit'