from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf.urls.static import static
from . import settings
from BookNest.converters import UnicodeSlugConverter

register_converter(UnicodeSlugConverter, 'uslug')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('users.urls')),
    path('', include('books.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)