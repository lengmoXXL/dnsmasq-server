from django.contrib import admin

from .models import DNSRecord

# Register your models here.


def apply_dns_records(model_admin, request, queryset):
    with open('/dnsmasq/hosts/dnsmasqhosts', 'w') as f:
        for item in queryset:
            f.write(f'{item.ip}\t{item.host}\n')


apply_dns_records.short_description = 'Apply Dns Record into dnsmasq hosts file'


@admin.register(DNSRecord)
class DNSRecordAdmin(admin.ModelAdmin):
    list_display = ('ip', 'host')
    actions = [apply_dns_records]
