from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    url("admin/", admin.site.urls),
    url(r"^", include("base.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
