from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('supersecret/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "My unnamed Social App Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to yet-to-be-named Portal"