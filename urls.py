from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update
from inventory.models import *

info_dict = {
    # 'queryset':ISCNode.objects.all(),
	'queryset':VirtualMachine.objects.order_by('name'),
}


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^$', list_detail.object_list, dict(info_dict, template_name='index.html'), name='homepage'),
    url(r'^system/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(info_dict, template_name='iscnode_detail.html'), name='system-display'),
)
