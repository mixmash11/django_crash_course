from django.shortcuts import render

from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context["my_statement"] = "Nice to see you!"
        return context

    def say_bye(self):
        return "Goodbye!"
