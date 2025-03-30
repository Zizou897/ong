from django.contrib import admin
from django.utils.safestring import mark_safe
import mimetypes
from .models import (
    Cas,
    Messages
)
# Register your models here.


@admin.register(Cas)
class CasAdmin(admin.ModelAdmin):
    list_display = ("media_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    
    def media_view(self, obj):
        if obj.picture_video:  # Vérifier si un fichier est présent
            mime_type, _ = mimetypes.guess_type(obj.picture_video.url)
            if mime_type and mime_type.startswith("image"):
                return mark_safe(f'<img src="{obj.picture_video.url}" style="height:100px; width:150px">')
            elif mime_type and mime_type.startswith("video"):
                return mark_safe(f'''
                    <video width="150" height="100" controls>
                        <source src="{obj.picture_video.url}" type="{mime_type}">
                        Votre navigateur ne supporte pas la lecture de vidéos.
                    </video>
                ''')
        return "Aucun média"

    # def image_view(self, obj):
    #     return mark_safe(f'<img src="{obj.picture_video.url}" style="height:100px; width:150px">')
    media_view.short_description = "Aperçu des images"


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "subject")
    date_hierarchy = "created_at"
    list_per_page = 10


