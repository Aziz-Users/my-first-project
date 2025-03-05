from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime 


def get_profile_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"user_{instance.user.username}.{ext}"
    return os.path.join('profile_pics/', filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_profile_image_upload_path, default='default.png')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username
