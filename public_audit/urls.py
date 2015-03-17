from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'public_audit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^client/', include('client.urls', namespace="client")),
    url(r'^admin/', include(admin.site.urls)),
)
