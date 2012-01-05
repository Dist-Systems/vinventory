from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update
from inventory.models import *

vm_dict = {
	'queryset':VirtualMachine.objects.order_by('name'),
}

dstore_dict = {
	'queryset':DataStore.objects.order_by('name'),
}

host_dict = {
	'queryset':VMHost.objects.order_by('name'),
}

urlpatterns = patterns('',
	url(r'^server/(?P<server_id>\d+)/$', 'inventory.views.server_detail', name='server-detail'),
  url(r'^system/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(vm_dict, template_name='vm_detail.html'), name='vm-detail'),
	url(r'^dstore/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(dstore_dict, template_name='datastore.html'), name='datastore'),
	url(r'^host/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(host_dict, template_name='host.html'), name='host'),
)