"""
Cheese views so we can talk about cheese
"""

from django.views.generic import ListView, DetailView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese
