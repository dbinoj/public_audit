from django.conf.urls import patterns, url

from auth import views

urlpatterns = patterns('',
    # /auth/
    url(r'^$', views.index, name='index'),
)