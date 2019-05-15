from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import jewelry
from django.db.models import Q
# Create your views here.


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            lookups = Q(description__icontains=query) | Q(slug__icontains=query)
            return jewelry.objects.filter(lookups).distinct()
        return None



