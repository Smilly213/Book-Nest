from django.urls import path, register_converter
from . import views
from .converters import UnicodeSlugConverter

register_converter(UnicodeSlugConverter, 'uslug')

urlpatterns = [
    path('add', views.AddProfile.as_view(), name='addprofile'),
    path('<uslug:profile_slug>', views.DetailProfile.as_view(), name='detailprofile'),
]
