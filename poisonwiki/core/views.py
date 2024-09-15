from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = "pages/landing.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)

        context["title"] = "PoisonWiki"
        return context
