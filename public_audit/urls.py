from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'public_audit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^client/', include('client.urls', namespace="client")),
<<<<<<< HEAD
    url(r'^tpa/', include('tpa.urls', namespace="tpa")),
    #url(r'^storage/', include('storage.urls', namespace="storage")),
=======
    url(r'^storage/', include('storage.urls', namespace="storage")),
>>>>>>> master
    url(r'^admin/', include(admin.site.urls)),
)
