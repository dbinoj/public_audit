from django.conf.urls import patterns, url

from authentication import views

urlpatterns = patterns('',
    # /auth/
    url(r'^$', views.index, name='index'),
)