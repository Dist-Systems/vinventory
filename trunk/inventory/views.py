from django.shortcuts import render_to_response
from inventory.models import *
from django.template import Context, loader, RequestContext
from django.http import HttpResponse


def test(request):
    latest_vendor_list = Vendor.objects.all()[:5]
    return render_to_response("test.html",  {'object_list': latest_vendor_list}, context_instance=RequestContext(request))	