from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update
from inventory.models import *

vm_dict = {
    # 'queryset':ISCNode.objects.all(),
	'queryset':VirtualMachine.objects.order_by('name'),
}

dstore_dict = {
    # 'queryset':ISCNode.objects.all(),
	'queryset':DataStore.objects.order_by('name'),
}

host_dict = {
    # 'queryset':ISCNode.objects.all(),
	'queryset':VMHost.objects.order_by('name'),
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

    url(r'^$', list_detail.object_list, dict(vm_dict, template_name='index.html'), name='homepage'),
    url(r'^test/$', 'inventory.views.test'),
    url(r'^system/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(vm_dict, template_name='vm_detail.html'), name='vm-detail'),
	url(r'^dstore/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(dstore_dict, template_name='datastore.html'), name='datastore'),
	url(r'^host/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(host_dict, template_name='host.html'), name='host'),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,'show_indexes': True }),
)