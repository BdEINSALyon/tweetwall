"""moderation URL configuration
"""
from django.conf.urls import url

from social import views

urlpatterns = [
    url(r'^screen/(?P<pk>[0-9]+)$', views.Screen.as_view(), name='screen')
]