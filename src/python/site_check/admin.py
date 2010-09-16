from django.contrib import admin
from site_check.models import SiteCheck

class SiteCheckAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active', 'added')
    list_editable = ('active',)

admin.site.register(SiteCheck, SiteCheckAdmin)



