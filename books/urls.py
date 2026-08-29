from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('addbook/', views.AddBook.as_view(), name='add_book'),
    path('<uslug:book_slug>/', views.DetailBook.as_view(), name='detail_book'),
    path('update/<uslug:slug>/', views.UpdateBook.as_view(), name='update_book')
]