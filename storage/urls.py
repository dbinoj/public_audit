from django.conf.urls import patterns, url

from storage import views

urlpatterns = patterns('',
    # /storage/
    url(r'^$', views.index, name='index'),
    # /storage/file/5/
    #url(r'^file/(?P<file_id>\d+)/$', views.ClientFile, name=''),

)
