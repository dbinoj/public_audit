from django.conf.urls import patterns, url

from tpa import views

urlpatterns = patterns('',
    # /tpa/
    url(r'^$', views.index, name='index'),
    # /storage/file/5/
   # url(r'^file/(?P<file_id>\d+)/$', views.file_detail, name='file_detail'),

)
