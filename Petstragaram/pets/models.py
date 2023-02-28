from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from Petstragaram.accounts.models import PetstagramUser


# Create your models here.
class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
