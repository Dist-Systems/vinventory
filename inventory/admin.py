from inventory.models import *
from django.contrib import admin

admin.site.register(VirtualMachine)
admin.site.register(Server)
admin.site.register(DataStore)
admin.site.register(IpAddress)
admin.site.register(Vendor)
admin.site.register(VMHost)