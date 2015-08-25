from django.views.generic.base import TemplateView

from accounts.models import Practice


class HomeView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['practices'] = Practice.objects.all()
        return context

home = HomeView.as_view()
