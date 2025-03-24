from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Cas,
    Messages
)
# Register your models here.


@admin.register(Cas)
class CasAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "subject")
    date_hierarchy = "created_at"
    list_per_page = 10


