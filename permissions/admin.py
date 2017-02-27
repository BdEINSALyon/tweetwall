from django.contrib import admin

from permissions import models
from permissions.forms import AzureGroupForm


@admin.register(models.AzureGroup)
class AzureGroupAdmin(admin.ModelAdmin):
    form = AzureGroupForm
