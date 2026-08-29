from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .forms import BookForm
from .models import Book

class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'

    def get_queryset(self):
        return Book.objects.all()

class DetailBook(DetailView):
    model = Book
    template_name = 'books/detail_book.html'
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, slug=self.kwargs[self.slug_url_kwarg])

class AddBook(CreateView):
    form_class = BookForm
    template_name = 'books/add_book.html'
    success_url = '/'

class UpdateBook(UpdateView):
    model = Book
    fields = ['image', 'title', 'genre', 'author', 'context', 'file']
    template_name = 'books/add_book.html'
