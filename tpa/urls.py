from django.conf.urls import patterns, url

from tpa import views

urlpatterns = patterns('',
    # /tpa/
    url(r'^$', views.index, name='index'),
    # /tpa/5/rts/
    url(r'^tpa/(?P<file_id>\d+)/rts/$', views.file_requestto_server, name='file_requestto_server'),
    # /tpa/5/verify/
    url(r'^tpa/(?P<file_id>\d+)/verify/$', views.verify, name='verify'),

)
