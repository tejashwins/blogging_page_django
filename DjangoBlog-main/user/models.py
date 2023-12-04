from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics', default='default.jpg')

    def save(self, *args, **kwargs):
         super().save(*args, **kwargs)

         img = Image.open(self.img.path)

         if img.height > 300 or img.width > 300:
             output_size = (300, 300)
             img.thumbnail(output_size)
             img.save(self.img.path)

    def __str__(self):
        return f"{self.user.username}'s profile"
