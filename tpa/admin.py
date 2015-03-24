from django.contrib import admin

# Register your models here.
from . import models
admin.site.site_header = 'Public_audit'
admin.site.site_title = 'Public_audit'
admin.site.register(models.AuditRequest)
