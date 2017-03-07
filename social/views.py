import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from social.models import Feed, Message


class Screen(DetailView):
    model = Feed
    template_name = 'social/screen.html'


class GetFeedData(View):

    def get(self, request, feed):
        messages_pub = Message.objects.filter(feed_id=feed, status=Message.PUBLISHED).order_by('-published_at')[:20]
        messages_pro = Message.objects.filter(feed_id=feed, status=Message.PROMOTED).order_by('-published_at')[:20]
        return HttpResponse(json.dumps({"data": {
            "published": [obj.as_dict() for obj in messages_pub],
            "promoted": [obj.as_dict() for obj in messages_pro],
        }}), content_type='application/json')
