from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'country.views.home', name='home'),
    # url(r'^ajaxproject/', include('ajaxproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'',include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'get-states/$','country.views.get_states'),
)
