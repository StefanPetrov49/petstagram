from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstragaram.common.urls')),
    path('accounts/', include('Petstragaram.accounts.urls')),
    path('pets/', include('Petstragaram.pets.urls')),
    path('photos/', include('Petstragaram.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
