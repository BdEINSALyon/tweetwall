from django import shortcuts
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from moderation.auth_mixin import ModerationPermissionMixin
from social.models import Feed, Message


class FeedList(ModerationPermissionMixin, ListView):
    model = Feed
    template_name = 'moderation/feeds.html'


class FeedDetail(ModerationPermissionMixin, DetailView):
    model = Feed
    template_name = 'moderation/feed.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FeedDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['message_list'] = Message.objects.filter(feed=context['object']).order_by('-published_at')
        return context


class FeedRefresh(ModerationPermissionMixin, View):
    http_method_names = ['post']

    def post(self, request, pk, **kwargs):
        feed = shortcuts.get_object_or_404(Feed, pk=pk)
        for provider in feed.providers.all():
            provider.provider_instance.fetch_messages(feed)
        return shortcuts.redirect('feed', pk=feed.pk)


class MessageModerate(ModerationPermissionMixin, View):
    http_method_names = ['get']

    def get(self, request, pk, state, **kwargs):
        message = shortcuts.get_object_or_404(Message, pk=pk)
        message.status = state
        message.save()
        return shortcuts.redirect('feed', pk=message.feed.pk)
