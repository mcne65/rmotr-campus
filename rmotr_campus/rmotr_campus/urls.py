from django.conf.urls import include, url
from django.contrib import admin

from accounts import views

urlpatterns = (
    # Third party apps
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

    # Own apps
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
)
