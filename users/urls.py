from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddProfile.as_view(), name='addprofile'),
    path('<uslug:profile_slug>/', views.DetailProfile.as_view(), name='detailprofile'),
]
