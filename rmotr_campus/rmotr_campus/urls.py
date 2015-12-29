from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = (
    # Third party apps
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

    # Own apps
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
)
