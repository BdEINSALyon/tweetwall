from django.contrib import admin

from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author_username', 'published_at', 'status', 'provider']
    list_display_links = ['author_username']
    list_editable = ['status']
    ordering = ['-published_at']


@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(models.Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['hashtag']
    list_display_links = ['hashtag']
    ordering = ['hashtag']

