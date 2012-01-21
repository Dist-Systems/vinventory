from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from inventory.forms import NewServerForm, EditServerForm
from inventory.models import *

def homepage(request):
    vendor_list = Vendor.objects.all()
    server_list = Server.objects.all()
    vm_list = VirtualMachine.objects.all()
    return render_to_response(
	    "index.html",
		{'vendor_list': vendor_list, 'server_list':server_list, 'vm_list':vm_list}, 
		context_instance=RequestContext(request))

def newServer(request): 
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = NewServerForm(request.POST)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/') 
    else:
        # An unbound form
        form = NewServerForm() 
    return render_to_response(
            'server_new.html', 
            { 'form': form,},  
            context_instance=RequestContext(request))
    
def editServer(request, server_id):
    # Which server will this form show?
    server = get_object_or_404(Server, pk=server_id)
    
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = EditServerForm(request.POST, instance=server)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST (to guard from accidentally reposting)
            return HttpResponseRedirect('/')
             
    # The form has not been submitted, it's a GET request 
    else:
        # A form that is bound to server data
        form = EditServerForm(instance=server) 
    return render_to_response(
            'server_edit.html', 
            { 'form': form, 'server_id':server.id},  
            context_instance=RequestContext(request))