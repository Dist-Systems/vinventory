from django.conf import settings
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # index: homepage
    url(r'^$', 'inventory.views.homepage', name='homepage'),
	
	# inventory urls
	url(r'^inventory/', include('inventory.urls')),

	
	# Static media 
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,'show_indexes': True }),
)