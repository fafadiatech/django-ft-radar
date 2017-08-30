from django.views.generic.base import ContextMixin

class BaseContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        kwargs['title'] = "Radar: Lead Monitoring System"
        kwargs['project_name'] = "Radar"
        kwargs['company_name'] = "Fafadia Tech"
        return kwargs