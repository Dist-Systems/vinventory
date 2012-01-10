from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update
from inventory.models import *

vm_dict = {
	'queryset':VirtualMachine.objects.all(),
	'template_object_name' : "vm",
}

dstore_dict = {
	'queryset':DataStore.objects.order_by('name'),
	'template_object_name' : "dstore",
}

host_dict = {
	'queryset':VMHost.objects.order_by('name'),
	'template_object_name' : "vmhost",
}

server_dict = {
	'queryset':Server.objects.order_by('name'),
	'template_object_name' : "server",
}


urlpatterns = patterns('',
  url(r'^list/servers/$', list_detail.object_list, dict(server_dict,template_name='server_list.html'), name='servers'),
	url(r'^server/(?P<server_id>\d+)/$', 'inventory.views.server_detail', name='server-detail'),
	url(r'^create/server/', 'inventory.views.newServer', name='newServer'),
	
	url(r'^virtual/$', list_detail.object_list, dict(vm_dict,template_name='vm_list.html'), name='virtual'),
	
  url(r'^vm/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(vm_dict, template_name='vm_detail.html'), name='vm-detail'),
	
  url(r'^dstore/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(dstore_dict, template_name='datastore.html'), name='datastore'),
	url(r'^host/(?P<object_id>[-\w]+)/', list_detail.object_detail, dict(host_dict, template_name='host.html'), name='host'),
)