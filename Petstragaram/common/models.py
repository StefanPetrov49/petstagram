from django.db import models

from Petstragaram.accounts.models import PetstagramUser
from Petstragaram.photos.models import Photo


# Create your models here.

class PhotoComment(models.Model):
    text = models.CharField(
        max_length=300
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE,
    )
