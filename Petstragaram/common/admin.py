from django.contrib import admin

from Petstragaram.common.models import PhotoLike, PhotoComment


# Register your models here.

@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass
