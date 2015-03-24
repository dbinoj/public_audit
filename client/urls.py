from django.conf.urls import patterns, url

from client import views

urlpatterns = patterns('',
    # /client/
    url(r'^$', views.index, name='index'),
    # /client/file/5/
    url(r'^file/(?P<file_id>\d+)/$', views.file_detail, name='file_detail'),
    # /client/file/5/request_audit/
    url(r'^file/(?P<file_id>\d+)/request_audit/$', views.file_request_audit, name='file_request_audit'),

)
