from __future__ import division, unicode_literals, absolute_import

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {}
