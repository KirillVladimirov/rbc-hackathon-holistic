from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # type: ignore
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)  # type: ignore

    def __str__(self):
        return self.user.username
