from inventory.models import *
from django.contrib import admin

class IPInline(admin.TabularInline):
    model = IpAddress
    extra = 3

class VirtualMachineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','notes','role','cpuCount','memoryMB']}),
        ('Location',               {'fields': ['host','datastore'],'classes': ['collapse']}),
        ('PowerState', {'fields': ['powerState'], 'classes': ['collapse']}),
    ]
    inlines = [IPInline]
    list_display = ('name', 'created', 'powerState')

admin.site.register(VirtualMachine,VirtualMachineAdmin)
admin.site.register(Server)
admin.site.register(DataStore)
admin.site.register(IpAddress)
admin.site.register(Vendor)
admin.site.register(VMHost)