from django.core.exceptions import ValidationError


def validate_image_file_size(image):
    if image.size > 5242880:
        raise ValidationError("The maximum image size is 5MB")