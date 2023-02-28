from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class PetstagramUser(AbstractUser):

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    choices = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (DO_NOT_SHOW, DO_NOT_SHOW),
    )

    first_name = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=30,
    )
    last_name = models.CharField(
        validators=[MinLengthValidator(2, 'Name must be more that 2 letters')],
        max_length=30,
    )
    email = models.EmailField(
        unique=True
    )
    gender = models.CharField(
        choices=choices,
        max_length=11,
    )
    profile_picture = models.URLField()

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
