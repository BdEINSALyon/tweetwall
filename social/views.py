from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from social.models import Feed


class Screen(DetailView):
    model = Feed
    template_name = 'social/screen.html'

