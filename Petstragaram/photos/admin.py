from django.contrib import admin

from Petstragaram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pets')

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'