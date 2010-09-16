from django.contrib import admin
from site_check.models import SiteCheck

class SiteCheckAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active', 'added')

admin.site.register(SiteCheck, SiteCheckAdmin)



