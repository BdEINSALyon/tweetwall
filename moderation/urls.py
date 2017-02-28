"""moderation URL configuration
"""
from django.conf.urls import url

from moderation import views

urlpatterns = [
    url(r'^feeds$', views.FeedList.as_view(), name='feeds'),
    url(r'^feed/(?P<pk>[0-9]+)$', views.FeedDetail.as_view(), name='feed'),
    url(r'^feed/(?P<pk>[0-9]+)/refresh$', views.FeedRefresh.as_view(), name='feed_refresh'),
    url(r'^message/(?P<pk>[0-9]+)/moderate/(?P<state>(PU|PR|RE))$', views.MessageModerate.as_view(), name='message_moderate')
]