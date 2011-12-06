from django.shortcuts import render_to_response
from inventory.models import *
from django.template import Context, loader, RequestContext
from django.http import HttpResponse


def test(request):
    latest_poll_list = IpAddress.objects.all().order_by('-address')[:5]
    return render_to_response("index.html",  {'object_list': latest_poll_list},
context_instance=RequestContext(request))	