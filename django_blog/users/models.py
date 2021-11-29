from django.db import models
from django.contrib.auth.models import User
from .resize import image_resize


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        image_resize(self.image, 300, 300)
        super().save(*args, **kwargs)
