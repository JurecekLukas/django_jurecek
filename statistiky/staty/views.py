from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
def index(request):

    return render(request, template_name='index.html')

class StatsListView(ListView):
    model = Statistiky
    context_object_name = 'staty_list'
    template_name = 'list.html'

class StatsDetailView(DetailView):
    model = Statistiky
    context_object_name = 'staty_detail'
    template_name = 'detail.html'