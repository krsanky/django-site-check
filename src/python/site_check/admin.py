from django.contrib import admin
from site_check.models import CheckSite
from site_check.models import CheckLog

class CheckSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active', 'added')
    list_editable = ('active',)
admin.site.register(CheckSite, CheckSiteAdmin)

class CheckLogAdmin(admin.ModelAdmin):
    list_display = ('site', 'status', 'time')
    ordering = ('time',)
admin.site.register(CheckLog, CheckLogAdmin)



