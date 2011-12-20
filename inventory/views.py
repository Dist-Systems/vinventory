from django.shortcuts import render_to_response, get_object_or_404
from inventory.models import *
from django.template import Context, loader, RequestContext
from django.http import HttpResponse


def test(request):
    latest_vendor_list = Vendor.objects.all()[:5]
    return render_to_response("test.html",  {'object_list': latest_vendor_list}, context_instance=RequestContext(request))

def homepage(request):
    vendor_list = Vendor.objects.all()
    server_list = Server.objects.all()
    vm_list = VirtualMachine.objects.all()
    return render_to_response(
	    "index.html",
		{'vendor_list': vendor_list, 'server_list':server_list, 'vm_list':vm_list}, 
		context_instance=RequestContext(request))

def server_detail(request, server_id):
    s = get_object_or_404(Server, pk=server_id)
    return render_to_response('server_detail.html', {'server': s})