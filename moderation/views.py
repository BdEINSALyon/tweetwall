from django import shortcuts
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from moderation.auth_mixin import ModerationPermissionMixin
from social.models import Feed


class FeedList(ModerationPermissionMixin, ListView):
    model = Feed
    template_name = 'moderation/feeds.html'


class FeedDetail(ModerationPermissionMixin, DetailView):
    model = Feed
    template_name = 'moderation/feed.html'


class FeedRefresh(ModerationPermissionMixin, View):
    http_method_names = ['post']

    def post(self, request, pk, **kwargs):
        feed = shortcuts.get_object_or_404(Feed, pk)
        for provider in feed.providers:
            provider.provider_instance.fetch_messages(feed)
        return shortcuts.redirect('feed', pk=feed.pk)
