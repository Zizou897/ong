from django.db import models
import mimetypes

from core.constants import (
    CAS_IMAGE_PATH
)
# Create your models here.



class Convention(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True




class Cas(Convention):
    title = models.CharField(max_length = 150)
    picture_video = models.FileField(upload_to=CAS_IMAGE_PATH, max_length = 100)
    description = models.TextField()

    class Meta:
        verbose_name = "Cas"
        verbose_name_plural = "cas"
        
    def __str__(self):
        return self.title
    
    def is_video(self):
        mime_type, _ = mimetypes.guess_type(self.picture_video.name)
        if mime_type:
            if  mime_type.startswith('video'):
                return 'video'
    
    def is_image(self):
        # Vérifier si le fichier est une image en fonction de son type MIME
        mime_type, _ = mimetypes.guess_type(self.picture_video.name)
        if mime_type:
            if  mime_type.startswith('image'):
                return 'image'


class Messages(Convention):
    name = models.CharField(max_length=254, blank=True, null=True)
    subject = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Messages"
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return self.email