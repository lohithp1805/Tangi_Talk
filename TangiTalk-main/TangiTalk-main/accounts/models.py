# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import os
def get_profile_image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]  # Retrieve the file extension
    return f"profile_images/{instance.user.username}{ext}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_profile_image_upload_path, blank=True)

    def __str__(self):
        return self.user.username
