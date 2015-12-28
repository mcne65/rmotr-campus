from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url('^', include('django.contrib.auth.urls')),
)
