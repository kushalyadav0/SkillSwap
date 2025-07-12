# assistant/admin.py
from django.contrib import admin
from .models import SwapRequest

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display  = ("id", "requester", "requestee", "offered_skill",
                     "wanted_skill", "status", "created_at")
    list_filter   = ("status", "created_at")
    search_fields = ("requester__username", "requestee__username",
                     "offered_skill", "wanted_skill")

