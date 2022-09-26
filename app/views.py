from django.views.generic.base import TemplateView


cnt = 0

class ABoutPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        global cnt
        cnt += 1
        # context dict
        return {**super().get_context_data(**kwargs), **{'count': cnt}} 